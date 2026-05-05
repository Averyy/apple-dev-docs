# Creating a foveated streaming client on visionOS

**Framework**: Foveated Streaming

Build a visionOS app that streams high-fidelity immersive content from a computer or the cloud using the Foveated Streaming framework.

**Availability**:
- visionOS 26.4+
- Xcode 26.4+

#### Overview

This sample app demonstrates how to implement foveated streaming in a visionOS app, allowing you to connect to a local or remote device and receive streamed content with controls for pausing, resuming, and disconnecting the session.

Foveated streaming is an advanced rendering technique that optimizes the sending of visual content by prioritizing image quality in the area where you’re looking while reducing detail in peripheral vision. In visionOS, the Foveated Streaming framework enables apps to stream high-quality content from a computer or the cloud to Apple Vision Pro while maintaining user privacy.

Common use cases include:

- High-fidelity gaming experiences streamed from a powerful computer.
- Professional applications like CAD software, 3D modeling tools, and scientific visualization streamed from a local device or the cloud.
- Remote desktop access with an optimized immersive presentation.

> **Note**: To test the end-to-end streaming flow, build a desktop application that manages authentication and streams content. For more information, see [`Streaming a CloudXR application to Apple Vision Pro with foveation`](streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation.md).

#### Configure the Sample Code Project

This sample project requires use of the [`com.apple.developer.foveated-streaming-session`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.foveated-streaming-session) entitlement. Add the entitlement to the Xcode project in the Signing & Capabilities tab.

Because this sample app uses foveated streaming, you can’t run this sample in Simulator — you’ll need to run it on a device. To run this sample, you’ll need the following:

- An Apple Vision Pro with visionOS 26.4 or later.

#### Create a Foveated Streaming Session

To stream foveated content from a computer or the cloud to Apple Vision Pro, first initialize a [`FoveatedStreamingSession`](foveatedstreamingsession.md):

```swift
struct FoveatedStreamingSampleApp: App {
    private let session = FoveatedStreamingSession()
    
    // ...
}
```

A [`FoveatedStreamingSession`](foveatedstreamingsession.md) allows you to establish a connection with a streaming endpoint, manage the connection life cycle, and access bidirectional data channels for custom data exchange.

The sample initializes the foveated streaming session directly in the main app structure so it’s accessible to the [`ImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace).

#### Define a Foveated Streaming Space

Create an immersive space to display streamed content for the session by defining an [`ImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace) in the app’s body:

```swift
struct FoveatedStreamingSampleApp: App {
    private let session = FoveatedStreamingSession()
    
    // ...

    var body: some Scene {
        
        // ...
        
        ImmersiveSpace(foveatedStreaming: session) {
            // ...
        }
        .immersionStyle(selection: .constant(.progressive), in: .progressive)
    }
}
```

The app allows the person to adjust the size of the streamed content relative to passthrough by applying the [`progressive`](https://developer.apple.com/documentation/SwiftUI/ImmersionStyle/progressive) immersion style, but you can also use the [`mixed`](https://developer.apple.com/documentation/SwiftUI/ImmersionStyle/mixed) or [`full`](https://developer.apple.com/documentation/SwiftUI/ImmersionStyle/full) immersion styles. When using the [`mixed`](https://developer.apple.com/documentation/SwiftUI/ImmersionStyle/mixed) immersion style, you can control the amount of passthrough with the alpha channel of your rendered content.

You can optionally add native [`RealityKit`](https://developer.apple.com/documentation/RealityKit) content alongside the streamed content by placing it inside a [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) in your immersive space. For examples, see `ReopenMainWindowView` or `TransformStreamWidgetView` in the downloadable sample code project.

#### Connect to a Streaming Session

The [`FoveatedStreamingSession`](foveatedstreamingsession.md) provides three ways to connect to a streaming endpoint:

- **System discovery:** Automatically discover nearby computers that are ready to stream content.
- **Local:** Manually connect to a computer on your local network using its IP address and port.
- **Remote:** Manually connect to a remote streaming endpoint using its URL and port.

System discovery allows the person to automatically connect to a streaming endpoint without having to specify its IP address. This is the recommended connection method for people in close proximity to their streaming computer and its display.

![A screenshot of a Connect to Stream dialog box showing the Automatic tab selected. The interface displays a Wi-Fi icon, explanatory text reading Discover nearby computers on your network, and a blue Search button at the bottom.](https://docs-assets.developer.apple.com/published/51d87b5b286afe4dd75b4f446c63ccef/connect-with-system-discovery%402x.png)

The sample initiates system discovery by calling the [`connect(endpoint:)`](foveatedstreamingsession/connect(endpoint:).md) method with the [`systemDiscovered`](foveatedstreamingsession/endpoint/systemdiscovered.md) parameter when the person presses the Search button:

```swift
try await session.connect(endpoint: .systemDiscovered)
```

Upon calling this method, visionOS presents the person with system UI that allows them to select a device from a list of nearby computers that are ready to stream content.

Alternatively, a person can connect to a streaming endpoint directly by entering its IP address and port.

![A screenshot of a Connect to Stream dialog box showing the Local IP tab selected. The interface displays a computer monitor icon, two input fields containing 1.1.1.1 and port 55000, and a blue Connect button at the bottom.](https://docs-assets.developer.apple.com/published/964ecc3cfa2d68a3c58d87bd3585b1a9/connect-with-ip-address%402x.png)

The sample initializes the IP address and port variables with [`AppStorage`](https://developer.apple.com/documentation/SwiftUI/AppStorage) so that the person doesn’t have to reenter them each time they use the app. The sample also converts them to [`IPv4Address`](https://developer.apple.com/documentation/Network/IPv4Address) and [`NWEndpoint.Port`](https://developer.apple.com/documentation/Network/NWEndpoint/Port) objects to validate them:

```swift
@AppStorage("ipAddress") private var ipAddress: String = "0.0.0.0"
@AppStorage("port") private var port: Int = 55000

// ...

var networkIPAddress: IPAddress? {
    IPv4Address(ipAddress)
}

var networkPort: NWEndpoint.Port? {
    NWEndpoint.Port(String(port))
}

var isIPAddressAndPortValid: Bool {
    networkPort != nil && networkIPAddress != nil
}
```

The sample initiates a direct connection with the [`local(ipAddress:port:)`](foveatedstreamingsession/endpoint/local(ipaddress:port:).md) endpoint:

```swift
try await session.connect(endpoint: .local(ipAddress: networkIPAddress, port: networkPort))
```

A person can also connect to a remote streaming endpoint that you host in the cloud.

![A screenshot of a Connect to a Stream dialog box showing the Remote tab selected. The interface displays a network icon, a dropdown picker containing the text Example Endpoint, and a blue Connect button at the bottom.](https://docs-assets.developer.apple.com/published/cbd7c29048740b26836ac0a196addeb0/connect-with-remote-server%402x.png)

The sample initiates a remote connection with the [`remote(serverName:signalingHeaders:)`](foveatedstreamingsession/endpoint/remote(servername:signalingheaders:).md) endpoint:

```swift
try await session.connect(endpoint: .remote(serverName: serverName, 
                                            signalingHeaders: ["test-header": "my-test"]))
```

Connect to a specific remote server by adding an entry to the [`ApprovedStreamingEndpoints`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ApprovedStreamingEndpoints) dictionary in your app’s `Info.plist` file with the server’s name as the key and the server’s URL as the value. The framework looks up the server URL from the `ApprovedStreamingEndpoints` dictionary with the server name you pass to the remote endpoint. You can use signaling headers to authenticate and manage the connection. For more information, see [`Connecting to a streaming function with a client`](https://developer.apple.comhttps://docs.nvidia.com/cloud-functions/user-guide/latest/cloud-function/function-creation.html#connecting-to-a-streaming-function-with-a-client).

After initiating a connection with the `.systemDiscovered` and `.local` connection methods, visionOS then has the person scan a QR code on the device they connected to. This performs authentication if it’s their first time establishing a connection to that streaming endpoint. For more information on how to authenticate a connection with Apple Vision Pro from your streaming application, see [`Establishing foveated streaming sessions with Apple Vision Pro`](establishing-foveated-streaming-sessions-with-apple-vision-pro.md).

After authenticating, visionOS displays a modal asking the person whether they want to begin sharing information about the approximate region where they’re looking and start streaming or cancel the connection. If the person cancels the connection, the [`connect(endpoint:)`](foveatedstreamingsession/connect(endpoint:).md) method throws a [`FoveatedStreamingSession.DisconnectReason`](foveatedstreamingsession/disconnectreason.md) error.

#### Allow People to Cancel the Connection

The sample app allows the person to cancel the connection operation before it completes by cancelling the connection task.

For example, the `StreamConnectionView` maintains a `connectionTask` state variable that it sets when the person starts a connection, and cancels if the person cancels the connection:

```swift
struct StreamConnectionView: View {
    // ...
    @State private var connectionTask: Task<Void, Error>? = nil

    var isConnecting: Bool {
        connectionTask != nil
    }

    // ...

    var body: some View {
        // ...
        Button {
            if !isConnecting {
                connectionTask = Task { @MainActor in
                    defer {
                        connectionTask = nil
                    }
                    // Asynchronously connect to a system discovered, local, or remote streaming endpoint.
                }
            } else {
                connectionTask?.cancel()
            }
        } label: {
            Text(isConnecting ? "Cancel" : "Connect")
                .frame(maxWidth: .infinity)
                .padding()
            
        }
        .tint(isConnecting ? .red : .blue )
        // ...
    }
}
```

Alternatively, you can call [`disconnect()`](foveatedstreamingsession/disconnect().md) to interrupt the connection. The [`pause()`](foveatedstreamingsession/pause().md) and [`resume()`](foveatedstreamingsession/resume().md) methods also support task cancellation.

#### Preview Interactions in the Simulator

The sample decouples views from their dependence on the Foveated Streaming framework by abstracting [`FoveatedStreamingSession`](foveatedstreamingsession.md) methods with an environment variable. This allows you to create mock behaviors for those methods within SwiftUI previews, despite the framework not being available for simulator, improving UI development and iteration.

The sample defines a `StreamActions` class with methods for the various [`FoveatedStreamingSession`](foveatedstreamingsession.md) actions:

```swift
@MainActor
@Observable
class StreamActions {
    let connect: (FoveatedStreamingSession.Endpoint) async throws -> Void
    let pause: () async throws -> Void
    let resume: () async throws -> Void
    let disconnect: () async throws -> Void
    
    init(connect: @escaping (FoveatedStreamingSession.Endpoint) async throws -> Void,
         pause: @escaping () async throws -> Void,
         resume: @escaping () async throws -> Void,
         disconnect: @escaping () async -> Void) {
        self.connect = connect
        self.pause = pause
        self.resume = resume
        self.disconnect = disconnect
    }
}
```

The sample makes the `FoveatedStreamingSession.Endpoint` symbol available in the simulator by declaring a mock version of it in a custom `FoveatedStreamingSimulator` framework that targets the simulator.

In the main app structure, the sample passes a `StreamActions` object to the environment with methods that invoke the respective [`FoveatedStreamingSession`](foveatedstreamingsession.md) methods:

```swift
Window("Main", id: appModel.mainWindowId) {
    ContentView(status: session.sessionStatus)
        // ...
        .environment(
            StreamActions(
                connect: { endpoint in
                    try await session.connect(endpoint: endpoint)
                },
                pause: {
                    try await session.pause()
                },
                resume: {
                    try await session.resume()
                },
                disconnect: {
                    await session.disconnect()
                }
            )
        )
        // ...
}
```

Views that invoke stream actions access it through the environment and call its methods. For example, the stream connection view uses this environment variable to initiate connections when the person presses a button:

```swift
private enum ConnectionMode {
    case systemDiscovered
    case local
    case remote
    // ...
}

private struct StreamConnectionView: View {
    @Environment(StreamActions.self) var streamActions
    // ...
    @State private var connectionMode: ConnectionMode = .systemDiscovered
    // ...
    var body: some View {
        // ...
        Button {
            // ...
            switch connectionMode {
                case .systemDiscovered:
                    try await streamActions.connect(.systemDiscovered)
                case .local:
                    guard let networkIPAddress, let networkPort else { return }
                    try await streamActions.connect(.local(ipAddress: networkIPAddress, port: networkPort))
                case .remote:
                    try await streamActions.connect(.remote(serverName: serverName,
                                                            signalingHeaders: ["test-header": "my-test"]))
            }
            // ...
        }
        // ...
    }
    // ...
}
```

This decouples views from being dependent on [`FoveatedStreamingSession`](foveatedstreamingsession.md) and allows you to create SwiftUI previews of their behavior directly in Xcode. For example, the preview for the `StreamConnectionView` is as follows:

```swift
#Preview {
    StreamConnectionView()
        .environment(
            StreamActions(
                connect: { _ in
                    try await Task.sleep(nanoseconds: .max)
                },
                pause: {},
                resume: {},
                disconnect: {}
            )
        )
}
```

#### Display the Streamed Content

To show the streamed content after the app establishes a connection to a streaming endpoint, open the `ImmersiveSpace`.

You can open the `ImmersiveSpace` manually with the [`openImmersiveSpace`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/openImmersiveSpace) environment variable, or you can set the [`immersivePresentationBehaviors`](foveatedstreamingsession/immersivepresentationbehaviors-swift.property.md) of the [`FoveatedStreamingSession`](foveatedstreamingsession.md) to define when the session automatically opens and dismisses the streaming space.

The sample automatically opens the streaming space when the session connects or resumes, and automatically closes it when the session pauses or disconnects by setting its [`immersivePresentationBehaviors`](foveatedstreamingsession/immersivepresentationbehaviors-swift.property.md) to [`automatic(_:_:)`](foveatedstreamingsession/immersivepresentationbehaviors-swift.struct/automatic(_:_:).md):

```swift
@Environment(\.openImmersiveSpace) var openImmersiveSpace
@Environment(\.dismissImmersiveSpace) var dismissImmersiveSpace
@Environment(FoveatedStreamingSession.self) var session

// ...

private func setImmersivePresentationBehavior() {     
   // Automatically present the foveated streaming space when the session connects or resumes,
   // and hide it when the session pauses or disconnects.    
   session.immersivePresentationBehaviors = .automatic(openImmersiveSpace, dismissImmersiveSpace) 
}
```

If your streaming application doesn’t have content ready to display immediately after establishing a foveated streaming connection, consider manually opening the foveated streaming space when you receive a message from the streaming application using a [`FoveatedStreamingSession.MessageChannel`](foveatedstreamingsession/messagechannel.md) instead.

> **Note**: To maintain user privacy, visionOS displays streamed content directly so that it isn’t accessible to your app process.

#### Monitor the Session Status

Observing the connection status is crucial for creating a responsive interface that adapts to the streaming session’s changing state. The [`status`](foveatedstreamingsession/status-swift.property.md) property reports the current state of the streaming session.

The sample’s main view, `ContentView`, uses [`status`](foveatedstreamingsession/status-swift.property.md) to conditionally render different views depending on the connection status:

```swift
struct ContentView: View {
   // ...
   let session: FoveatedStreamingSession

   var isDisconnected: Bool {
       switch session.status {
           case .disconnected, .initialized, .connecting: true
           default: false
       }
   }

   var body: some View {
       // ...
       VStack {
           if isDisconnected {
               StreamConnectionView()
                   .transition(.opacity.combined(with: .scale))
           } else {
               StreamControlsView(status: session.status)
                   .transition(.opacity.combined(with: .scale))
           }
       }
       // ...
   }
}
```

When the session isn’t connected, the sample displays a view that allows people to connect to the stream. When connected to the session, the sample displays a view that presents a person with controls for pausing, resuming, and disconnecting the stream.

#### Handle Connection Errors

Connection issues are inevitable in networked applications, so a robust error handling strategy is essential for providing a good experience.

When the session status becomes [`FoveatedStreamingSession.Status.disconnected(_:)`](foveatedstreamingsession/status-swift.enum/disconnected(_:).md) for an unknown [`FoveatedStreamingSession.DisconnectReason`](foveatedstreamingsession/disconnectreason.md), the sample displays an alert with the error:

```swift
struct ContentView: View {
    // ...

    @State var isShowingDisconnectAlert = false
    @State var disconnectReason: String? = nil
    
    let session: FoveatedStreamingSession
    
    var body: some View {
        VStack {
            // ...
        }
        .onChange(of: session.status) {
            if case .disconnected(let disconnectReason) = session.status,
               disconnectReason != .appInitiatedDisconnect,
               disconnectReason != .unauthorized,
               disconnectReason != .endpointInitiatedDisconnect {
                disconnectReasonDescription = disconnectReason.errorDescription
                isShowingDisconnectAlert = true
            }
        }
        .alert(disconnectReasonDescription ?? "Unknown Reason", isPresented: $isShowingDisconnectAlert) {
            Button("OK") { }
        }
        // ...
    }
}
```

The sample app doesn’t display an error message when the `DisconnectReason` is [`appInitiatedDisconnect`](foveatedstreamingsession/disconnectreason/appinitiateddisconnect.md), [`unauthorized`](foveatedstreamingsession/disconnectreason/unauthorized.md), or [`endpointInitiatedDisconnect`](foveatedstreamingsession/disconnectreason/endpointinitiateddisconnect.md) as these are caused intentionally by the person using the app. For design guidance on when to display alerts, see Human Interface Guidelines > [`Alerts`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/alerts).

#### Manage Streaming Controls

After a [`FoveatedStreamingSession`](foveatedstreamingsession.md) establishes a connection, you can pause, resume, and disconnect from the session at any time with the [`pause()`](foveatedstreamingsession/pause().md), [`resume()`](foveatedstreamingsession/resume().md), and [`disconnect()`](foveatedstreamingsession/disconnect().md) methods.

As with the connection methods, the app passes these methods to the rest of the views in the app with the `StreamActions` environment variable.

When connected, the app displays a control interface in `StreamControlsView` that allows the person to pause, resume, or disconnect the streaming session:

The `StreamControlsView` is as follows:

```swift
struct StreamControlsView: View {
    @Environment(StreamActions.self) var streamActions
    
    @ScaledMetric var scaledButtonWidth = 40
    @ScaledMetric var scaledControlsWidth = 480
    
    @State var isSettingsVisible = false
    
    let status: FoveatedStreamingSession.Status
    
    var isSessionStatusUpdating: Bool {
        status == .pausing || status == .resuming || status == .disconnecting
    }

    var isSessionPaused: Bool {
        status == .paused
    }
    
    var isSessionDisconnecting: Bool {
        status == .disconnecting
    }
    
    var isSessionPausingOrResuming: Bool {
        status == .pausing || status == .resuming
    }

    var isDisplayingFullControls: Bool {
        isSettingsVisible || isSessionPaused || status == .pausing
    }
    
    var body: some View {
        VStack {
            HStack {
                ConnectionActionButton(
                    isLoading: isSessionDisconnecting,
                    systemImage: "stop.fill",
                    help: "Disconnect",
                    width: scaledButtonWidth,
                    action: streamActions.disconnect
                )
                .disabled(isSessionStatusUpdating)
                
                Button {
                    withAnimation(.easeInOut) {
                        isSettingsVisible.toggle()
                    }
                } label: {
                    Image(systemName: isSettingsVisible ? "arrow.down.right.and.arrow.up.left.circle.fill" : "gearshape.circle.fill")
                        .font(.title.scaled(by: 4))
                        .contentTransition(.symbolEffect(.replace, options: .speed(2.0)))
                }
                .buttonBorderShape(.circle)
                .buttonStyle(.borderless)
                .help(isSettingsVisible ? "Close Settings" : "Open Settings")
                
                ConnectionActionButton(
                    isLoading: isSessionPausingOrResuming,
                    systemImage: isSessionPaused ? "play.fill" : "pause.fill",
                    help: isSessionPaused ? "Resume" : "Pause",
                    width: scaledButtonWidth,
                    action: isSessionPaused ? streamActions.resume : streamActions.pause
                )
                .disabled(isSessionStatusUpdating)
            }
            .padding(.horizontal, 12)
            .glassBackgroundEffect()
            .hoverEffect { effect, isActive, proxy in
                effect.animation(.default.delay(isActive ? 0.0 : 0.2)) {
                    $0.clipShape(.capsule.size(
                        width: (isActive || isDisplayingFullControls) ? proxy.size.width : proxy.size.height,
                        height: proxy.size.height,
                        anchor: .center
                    ))
                }
            }
            
            if isSettingsVisible {
                DeveloperSettingsView()
                    .transition(.scale)
            }
        }
        .frame(width: scaledControlsWidth, height: isSettingsVisible ? 850 : nil)
    }
}
```

When a person looks at the controls, the sample uses [`hoverEffect(in:isEnabled:body:)`](https://developer.apple.com/documentation/SwiftUI/View/hoverEffect(in:isEnabled:body:)) to expand the controls, or hide the controls when they look away. This ensures that the controls don’t interfere with the streamed content, allowing the person to position them wherever is most convenient in their environment.

After pressing the button in the center of the `StreamControlsView`, the view expands to include additional controls. While this sample uses the expanded view to demonstrate other surfaces of the `FoveatedStreaming` API, you can adapt it to your app’s needs. For example, you can add app-specific controls that don’t fit in the minimized view, or remove the expanded view entirely if all of the controls fit within the `StreamControlsView`.

> **Note**: A person can pause and disconnect the stream at any time from Control Center or by returning to the home screen. You may choose to provide redundant controls within your experience for these actions or defer to the system provided controls.

#### Allow People to Reopen the Main Window

In some cases, such as when a person closes the main window by accident, you can provide a way to reopen the app’s main window without having them return to the home screen and break their immersion from the immersive streaming space.

The sample demonstrates one potential approach to this by tracking the visibility of the main window and displaying a button in the immersive space that allows people to reopen the main window if it’s no longer visible.

The sample’s `AppModel` includes a `WindowState` enumeration that tracks whether the main window is open or closed:

```swift
class AppModel {
    enum WindowState {
        case open(scenePhase: ScenePhase)
        case closed
        
        var isVisible: Bool {
            switch self {
                case .open(let scenePhase):
                    scenePhase != .background
                case .closed:
                    false
            }
        }
    }
    
    var mainWindowState = WindowState.closed
    let mainWindowId = "main"
}
```

The `.open` state has an associated value to store the [`ScenePhase`](https://developer.apple.com/documentation/SwiftUI/ScenePhase) of the window, which is useful for determining its visibility.

The sample defines the `TrackWindowStateViewModifier` to track the state of a window:

```swift
extension View {
    func trackWindowState(_ windowState: Binding<AppModel.WindowState>) -> some View {
        modifier(TrackWindowStateViewModifier(windowState: windowState))
    }
}

struct TrackWindowStateViewModifier: ViewModifier {
    @Environment(\.scenePhase) var scenePhase
    @Binding var windowState: AppModel.WindowState

    func body(content: Content) -> some View {
        content
            .onAppear() {
                windowState = .open(scenePhase: scenePhase)
            }
            .onDisappear() {
                windowState = .closed
            }
            .onChange(of: scenePhase) {
                windowState = .open(scenePhase: scenePhase)
            }
    }
}
```

> **Note**: When closing the last window in a visionOS app, its [`onDisappear(perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onDisappear(perform:)) modifier isn’t called. Instead, the scene phase of the window enters the background state. While you can use scene phase to determine window visibility, note that windows also enter the background state when inactive (such as when a person places a window behind them or focuses on another app). This means `isVisible` can return `false` for open but inactive windows.

The sample applies the custom `trackWindowState` modifier inside `ContentView` to track its state:

```swift
struct ContentView: View {
    // ...
    var body: some View {
        @Bindable var appModel = appModel
        VStack {
            // ...
        }
        // ...
        .trackWindowState($appModel.mainWindowState)
    }
}
```

In `ReopenMainWindowView`, the app displays an entity with button attachment to reopen the main window if it detects that the main window isn’t visible:

```swift
struct ReopenMainWindowView: View {
    @Environment(AppModel.self) private var appModel
    @Environment(\.openWindow) private var openWindow

    let reopenMainWindowEntity = Entity()
    
    var body: some View {
        RealityView { content in
            reopenMainWindowEntity.components.set(ViewAttachmentComponent(rootView:
                Button("Open Controls", systemImage: "arrow.up.left.and.arrow.down.right") {
                    openWindow(id: appModel.mainWindowId)
                }
                .breakthroughEffect(.subtle)
            ))
            reopenMainWindowEntity.components.set(OpacityComponent(opacity: 0))
            reopenMainWindowEntity.position = [0, 1, -1]
            content.add(reopenMainWindowEntity)
        }
        .onChange(of: appModel.mainWindowState.isVisible, initial: true) {
            // Show the reopen button when the main window isn't visible and hide it otherwise.
            Entity.animate(appModel.mainWindowState.isVisible ? .easeOut(duration: 0.25) : .easeIn(duration: 0.25)) {
                reopenMainWindowEntity.components[OpacityComponent.self]?.opacity = appModel.mainWindowState.isVisible ? 0 : 1
            }
        }
    }
}
```

#### Adjust the Origin of the Streamed Content

The [`immersiveSpaceFromRemoteSceneTransform`](foveatedstreamingsession/immersivespacefromremotescenetransform.md) defines the spatial relationship between the origin of the streamed content and the foveated streaming space. By default, the remote scene origin matches the immersive space origin, but you can adjust the `immersiveSpaceFromRemoteSceneTransform` to modify the position and orientation of the streamed content within your immserive space.

The `TransformStreamWidgetView` attaches a [`DragGesture`](https://developer.apple.com/documentation/SwiftUI/DragGesture) to an entity and updates the `immersiveSpaceFromRemoteSceneTransform` based on its translation as the person moves it around:

```swift
struct TransformStreamWidgetView: View {
#if !targetEnvironment(simulator)
    @Environment(FoveatedStreamingSession.self) private var session
#endif
    
    let originPosition: SIMD3<Float> = [0, 0.75, -1]
    @State var dragStartPosition: SIMD3<Float> = .zero
    @State var isDragging: Bool = false
    
    var body: some View {
        RealityView { content in
            // Create an entity with a sphere model that can receive system input.
            let transformWidget = Entity(
                // ...
            )
            // Apply a drag gesture to the entity that moves it around the scene.
            transformWidget.components.set(GestureComponent(
                DragGesture(minimumDistance: 0).targetedToEntity(transformWidget)
                    .onChanged { value in
                        // Initialize the drag.
                        if !isDragging {
                            dragStartPosition = transformWidget.position
                            isDragging = true
                        }
                        // Update the entity position with the drag translation.
                        transformWidget.position = dragStartPosition + SIMD3<Float>(value.translation3D)
#if !targetEnvironment(simulator)
                        // Update the remote scene relative to the immersive space by the entity's total translation.
                        let translation = originPosition - transformWidget.position
                        session.immersiveSpaceFromRemoteSceneTransform = Transform(translation: translation).matrix
#endif
                    }.onEnded { value in
                        // End the drag.
                        isDragging = false
                    })
            )
            transformWidget.position = originPosition
            // ...
            content.add(transformWidget)
        }
    }
}
```

Use this transform to reposition and synchronize your streamed content with the immersive space.

> **Note**: Since streamed content is positioned relative to the immersive space, recentering your view with the Digital Crown will move the streamed content in tandem with the immersive space.

#### Send and Receive Data with Message Channels

The sample app initializes a `MessageChannelModel` on start up, which observes [`availableMessageChannels`](foveatedstreamingsession/availablemessagechannels.md) to know when the streaming application creates new message channels:

```swift
class MessageChannelModel {
    let session: FoveatedStreamingSession
    var availableChannels: [FoveatedStreamingSession.MessageChannel.ID: FoveatedStreamingSession.MessageChannel] = [:]
    var receivedMessagesByChannelId: [FoveatedStreamingSession.MessageChannel.ID: [String]] = [:]
    
    // ...
    
    init(session: FoveatedStreamingSession) {
        self.session = session
        // Listen for changes to the available message channels.
        monitorAvailableChannels()
    }
    
    private func monitorAvailableChannels() {
        withObservationTracking {
            for channelId in session.availableMessageChannels {
                setUpMessageChannel(for: channelId)
            }
        } onChange: {
            Task { @MainActor in
                self.monitorAvailableChannels()
            }
        }
    }

    // ...
}
```

The `setUpMessageChannel` method calls [`messageChannel(for:)`](foveatedstreamingsession/messagechannel(for:).md) to get a [`FoveatedStreamingSession.MessageChannel`](foveatedstreamingsession/messagechannel.md) object for channels it doesn’t already hold a reference to:

```swift

private func setUpMessageChannel(for channelId: FoveatedStreamingSession.MessageChannel.ID) {
    // Skip channels that are already set up.
    guard availableChannels[channelId] == nil,
            let messageChannel = session.messageChannel(for: channelId) else {
        return
    }
    // Save the channel.
    availableChannels[channelId] = messageChannel
    // Start receiving messages for the channel.
    startReceivingMessages(for: messageChannel)
}
```

The `setUpMessageChannel` also calls the `startReceivingMessages` method, which initiates a task to await the asynchronous stream of messages the [`receivedMessageStream`](foveatedstreamingsession/messagechannel/receivedmessagestream.md) provides and append them to an array of received messages for that channel:

```swift
private func startReceivingMessages(for channel: FoveatedStreamingSession.MessageChannel) {
    // Initialize an array to store messages the channel receives.
    receivedMessagesByChannelId[channel.id] = []
    // Dispatch a task to asynchronously append new messages as the channel receives them.
    Task {
        for await message in channel.receivedMessageStream {
            if let messageString = String(data: message, encoding: .utf8) {
                receivedMessagesByChannelId[channel.id]?.append(messageString)
            }
        }
    }
}
```

The sample sends messages by calling [`sendMessage(_:)`](foveatedstreamingsession/messagechannel/sendmessage(_:).md) when a person presses a button in the `MessageChannelView`:

```swift
private func sendMessage(message: Data, channel: FoveatedStreamingSession.MessageChannel) throws {
    try channel.sendMessage(message)
}
```

While this sample sends and receives messages as strings, consider utilizing a structured data format like JSON when sending messages.

## See Also

- [Streaming a CloudXR application to Apple Vision Pro with foveation](streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation.md)
  Integrate NVIDIA CloudXR™ and the session management connection protocol into your desktop or cloud application to stream high-fidelity spatial content to Apple Vision Pro.
- [Establishing foveated streaming sessions with Apple Vision Pro](establishing-foveated-streaming-sessions-with-apple-vision-pro.md)
  Discover, pair, and manage streaming sessions between Apple Vision Pro and local streaming endpoints by implementing the session management connection protocol.
- [Analyzing the performance of a foveated streaming session](analyzing-the-performance-of-a-foveated-streaming-session.md)
  Use the Foveated Streaming Statistics instrument to evaluate the performance of your visionOS streaming client app.
- [class FoveatedStreamingSession](foveatedstreamingsession.md)
  A session that manages a foveated streaming connection to a local or remote streaming endpoint.
- [struct FoveatedStreamingSpaceContent](foveatedstreamingspacecontent.md)
  A type that defines the content of an immersive space displaying a foveated stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/creating-a-foveated-streaming-client-on-visionos)*