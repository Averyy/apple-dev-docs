# Managing your Metal app window in iPadOS

**Framework**: Metal  
**Role**: Article

Set up a window that handles dynamically resizing your Metal content.

#### Overview

A scene represents a single instance of your app’s UI. You can choose whether people can create multiple scenes for your app. Typically, Metal apps and games support only one scene because they need priority access to the available resources on a device. On iPadOS 26 and later, people can always resize your app’s scenes if they have enabled multitasking.

Apps that don’t adopt the scene-based life cycle log a warning at startup on iOS 26 and iPadOS 26 and must be updated. In the next major release, the scene-based life cycle is required when building with the latest SDK.

> ❗ **Important**: Because [`UIRequiresFullScreen`](../BundleResources/information-property-list/uirequiresfullscreen.md) is deprecated, you can no longer opt out of iPad multitasking and dynamic resizing.

For more information on migrating your iPad app, see [TN3192: Migrating your app from the deprecated UIRequiresFullScreen key](../Technotes/tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md) and [TN3187: Migrating to the UIKit scene-based life cycle](../Technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle.md).

#### Create the window

Manage windows on iPad by using [`UIWindowScene`](../UIKit/uiwindowscene.md) for UIKit and [`Scene`](../SwiftUI/scene.md) for SwiftUI. To configure a [`UIWindow`](../UIKit/uiwindow.md) under a scene you assign a content view controller and embed your Metal view inside the controller.

To configure scene support for your Metal project:

1. Open the Xcode project.
2. Select the project in the Project navigator.
3. Select the app target.
4. Navigate to the General tab.
5. In the Deployment Info section, select “Scene manifest”.
6. Add the [`UIApplicationSceneManifest`](../BundleResources/information-property-list/uiapplicationscenemanifest.md) key if it doesn’t already exist.
7. Configure the dictionary value for your project.

**Swift**:

```json
<key>UIApplicationSceneManifest</key>
<dict>
    <key>UIApplicationSupportsMultipleScenes</key>
    <false/> 
    <key>UISceneConfigurations</key>
    <dict>
        <key>UIWindowSceneSessionRoleApplication</key>
        <array>
            <dict>
                <key>UISceneConfigurationName</key>
                <string>Default Configuration</string>
                <key>MyCustomSceneDelegateClass</key>
                <string>$(PRODUCT_MODULE_NAME).SceneDelegate</string>
                <key>UISceneStoryboardFile</key>
                <string>Main</string> 
                <key>UISceneClassName</key>
                <string>UIWindowScene</string> 
            </dict>
        </array>
    </dict>
</dict>
```

**Objective-C**:

```json
<key>UIApplicationSceneManifest</key>
<dict>
    <key>UIApplicationSupportsMultipleScenes</key>
    <false/> 
    <key>UISceneConfigurations</key>
    <dict>
        <key>UIWindowSceneSessionRoleApplication</key>
        <array>
            <dict>
                <key>UISceneConfigurationName</key>
                <string>Default Configuration</string>
                <key>MyCustomSceneDelegateClass</key>
                <string>SceneDelegate</string>
                <key>UISceneStoryboardFile</key>
                <string>Main</string> 
                <key>UISceneClassName</key>
                <string>UIWindowScene</string> 
            </dict>
        </array>
    </dict>
</dict>
```

To provide dynamic scene configurations for complex scenes that require fine-grained control, implement [`application(_:configurationForConnecting:options:)`](../UIKit/uiapplicationdelegate/application%28_,configurationforconnecting,options%29.md) for UIKit and [`UIApplicationDelegateAdaptor`](../SwiftUI/uiapplicationdelegateadaptor.md) for apps that uses the SwiftUI life cycle. This allows for providing dynamic scene configurations:

**Swift**:

```swift
@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(
        _ application: UIApplication,
        configurationForConnecting connectingSceneSession: UISceneSession,
        options: UIScene.ConnectionOptions
    ) -> UISceneConfiguration {

        // Each scene configuration has a unique, app-specific configuration 
        // name that you use to identify the scene. The configuration
        // name corresponds to entries in the `Info.plist` scene manifest.
        var configurationName: String!
    
        // An activity type distinguishes which scene to create.
        switch options.userActivities.first?.activityType {
        case "com.apple.gallery.openInspector":
            // Create a photo inspector window scene.
            configurationName = "Inspector Configuration"
        default:
            // Create a default gallery window scene.
            configurationName = "Default Configuration"
        }
        
        return UISceneConfiguration(
            name: configurationName,
            sessionRole: connectingSceneSession.role
        )
    }

    // The system calls this delegate when a person dismisses a scene 
    // session, like when closing a window.
    // 
    // If the system ends a session while the app wasn't running, it 
    // calls application(_:didDiscardSceneSessions:) shortly after 
    // calling `application(_:didFinishLaunchingWithOptions:)`.
    // 
    // Use this method to release scene-specific resources for the 
    // scene, as they won't return.
    func application(_ application: UIApplication, 
                     didDiscardSceneSessions sceneSessions: Set<UISceneSession>) {
    
    }
}
```

**Objective-C**:

```objc
- (UISceneConfiguration *)application:(UIApplication *)application 
                          configurationForConnectingSceneSession:(UISceneSession *)connectingSceneSession 
                          options:(UISceneConnectionOptions *)options {
                          
    // Each scene configuration has a unique, app-specific configuration 
    // name that you use to identify the scene. The configuration
    // name corresponds to entries in the `Info.plist` scene manifest.
    NSString *configurationName;

    // An activity type distinguishes which scene to create.
    NSString *activityType = options.userActivities.allObjects.firstObject.activityType;

    if ([activityType isEqualToString:@"com.apple.gallery.openInspector"]) {
        // Create a photo inspector window scene.
        configurationName = @"Inspector Configuration";
    } else {
        // Create a default gallery window scene.
        configurationName = @"Default Configuration";
    }

    return [[UISceneConfiguration alloc] initWithName: configurationName
                                         sessionRole: connectingSceneSession.role];
}

// The system calls this delegate when a person dismisses a scene 
// session, like when closing a window.
// 
// If the system ends a session while the app wasn't running, it 
// calls application(_:didDiscardSceneSessions:) shortly after 
// calling `application(_:didFinishLaunchingWithOptions:)`.
// 
// Use this method to release scene-specific resources for the 
// scene, as they won't return.
- (void)application:(UIApplication *)application 
        didDiscardSceneSessions:(NSSet<UISceneSession *> *)sceneSessions {
        
}
```

For more information on dynamic configuration, see [TN3187: Migrating to the UIKit scene-based life cycle](../Technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle.md). For more information on adding scene support to your app, see [Specifying the scenes your app supports](../UIKit/specifying-the-scenes-your-app-supports.md).

#### Choose the content size and style of your window

After adding scene support, configure the initial size and style of your window’s scenes. When your app creates or restores an instance of your user interface, the system calls [`scene(_:willConnectTo:options:)`](../UIKit/uiscenedelegate/scene%28_,willconnectto,options%29.md). This delegate method provides a window scene that you use to configure size contraints and style. For Metal apps and games, this is typically a single scene.

Use [`UISceneSizeRestrictions`](../UIKit/uiscenesizerestrictions.md) to constrain the minimum size you want, and to handle aspect ratio changes:

**Swift**:

```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    var window: UIWindow?

    func scene(_ scene: UIScene,
               willConnectTo session: UISceneSession,
               options connectionOptions: UIScene.ConnectionOptions) {

        guard let windowScene = scene as? UIWindowScene else { return }
        windowScene.sizeRestrictions?.minimumSize.width = 640.0
    }
}
```

**Objective-C**:

```objc
- (void)scene:(UIScene *)scene
        willConnectToSession:(UISceneSession *)session
        options:(UISceneConnectionOptions *)connectionOptions {

    UIWindowScene *windowScene = (UIWindowScene *)scene;
    if (![windowScene isKindOfClass:[UIWindowScene class]]) {
      return;
    }

    windowScene.sizeRestrictions.minimumSize = CGSizeMake(640.0,
                                                          windowScene.sizeRestrictions.minimumSize.height);
}        
```

In SwiftUI, use the [`windowResizability(_:)`](../SwiftUI/scene/windowresizability%28_%29.md) modifier to allow your scene’s content to provide sizing information:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
               .frame(minWidth: 640, minHeight: 360)
        }
        .windowResizability(.contentMinSize)
    }
}
```

To get the display scale, access [`displayScale`](../UIKit/uitraitcollection/displayscale.md) from [`UITraitCollection`](../UIKit/uitraitcollection.md) and perform necessary updates in [`viewIsAppearing(_:)`](../UIKit/uiviewcontroller/viewisappearing%28_%29.md). To calculate the pixel values you use for updating the size of [`MTLDrawable`](./mtldrawable.md), multiply the view’s frame and the [`contentsScale`](../QuartzCore/calayer/contentsscale.md) of your [`CAMetalLayer`](../QuartzCore/cametallayer.md):

**Swift**:

```swift
guard let metalLayer = view.layer as? CAMetalLayer else {
    return
}
// Get the scale that matches the window's display scale.
let screenScale = metalLayer.contentsScale

// Calculate the drawable size in pixels.
let sizeInPixels = CGSize(width: view.frame.width * screenScale,
                          height: view.frame.height * screenScale)
metalLayer.drawableSize = sizeInPixels
```

**Objective-C**:

```objc
CAMetalLayer *metalLayer = (CAMetalLayer *)self.view.layer;
if (![metalLayer isKindOfClass:[CAMetalLayer class]]) {
    return;
}
// Get the scale that matches the window's display scale.
CGFloat screenScale = metalLayer.contentsScale;

// Calculate the drawable size in pixels.
CGSize sizeInPixels = CGSizeMake(self.view.frame.size.width * screenScale,
                                 self.view.frame.size.height * screenScale);
metalLayer.drawableSize = sizeInPixels;
```

When a person resizes a window, it’s possible that the Metal view only renders to a portion of the window. In this case, add a launch screen with a black background color to letterbox the presentation, then configure the content gravity property for your view so drawable content scales uniformly.

![A screenshot of the Xcode information property list file that shows metadata](https://developer.apple.com/tutorials/images/com.apple.metal/managing-your-metal-app-window-in-ipados-launch-screen-1@2x.png)

**Swift**:

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    guard let metalLayer = view.layer as? CAMetalLayer else { return }

    metalLayer.isOpaque = true
    metalLayer.backgroundColor = UIColor.black.cgColor
    
    // For a game, set the content gravity so the aspect ratio of your
    // drawable scene scales uniformly to avoid squishing your content.
    metalLayer.contentsGravity = .resizeAspect
}
```

**Objective-C**:

```objc
- (void)viewDidLoad {
    [super viewDidLoad];

    CAMetalLayer *metalLayer = (CAMetalLayer *)self.view.layer;
    if (![metalLayer isKindOfClass:[CAMetalLayer class]]) {
        return;
    }

    metalLayer.opaque = YES;
    metalLayer.backgroundColor = [UIColor blackColor].CGColor;
    
    // For a game, set the content gravity so the aspect ratio of your
    // drawable scene scales uniformly to avoid squishing your content.
    metalLayer.contentsGravity = kCAGravityResizeAspect;
}
```

#### Handle window resizing

When resizing a window, the system sets [`isInteractivelyResizing`](../UIKit/uiwindowscene/geometry/isinteractivelyresizing.md) and calls the scene delegate
[`windowScene(_:didUpdateEffectiveGeometry:)`](../UIKit/uiwindowscenedelegate/windowscene%28_,didupdateeffectivegeometry%29.md) to allow for an app to handle window size changes. When a window resizes, continue rendering at the existing render target size until a person stops resizing the window, at which point you can update the new render target size. Don’t query the window size while a person is resizing a window. Instead, track the state in your renderer and then perform the necessary render size update when the person finishes resizing the window. For more information on responding to scene size changes, see [TN3187: Migrating to the UIKit scene-based life cycle](../Technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle.md).

If you use [MetalKit](../MetalKit/MetalKit.md), your app receives the [`mtkView(_:drawableSizeWillChange:)`](../MetalKit/mtkviewdelegate/mtkview%28_,drawablesizewillchange%29.md) delegate view callback:

**Swift**:

```swift
func mtkView(_ view: MTKView, drawableSizeWillChange size: CGSize) {

    /// Your code that responds to drawable size or orientation changes.

    /// Update the projection matrix with the new aspect size.
    let aspect = Float(size.width / size.height)
    projectionMatrix = matrix_perspective_right_hand(fovyRadians: 65.0 * (.pi / 180.0),
                                                     aspect: aspect,
                                                     nearZ: 0.1,
                                                     farZ: 100.0)
}

func matrix_perspective_right_hand(fovyRadians: Float,
                                   aspect: Float,
                                   nearZ: Float,
                                   farZ: Float) -> matrix_float4x4 {
    let ys = 1 / tanf(fovyRadians * 0.5)
    let xs = ys / aspect
    let zs = farZ / (nearZ - farZ)

    return matrix_float4x4(columns: (
      simd_float4(xs,  0,        0,  0),    // Column 0
      simd_float4( 0, ys,        0,  0),    // Column 1
      simd_float4( 0,  0,       zs, -1),    // Column 2
      simd_float4( 0,  0, nearZ * zs, 0)    // Column 3
    ))
}
```

**Objective-C**:

```objc
- (void)mtkView:(nonnull MTKView *)view 
        drawableSizeWillChange:(CGSize)size {
        
    /// Your code that responds to drawable size or orientation changes.

    /// Update the projection matrix with the new aspect size.
    float aspect = size.width / (float)size.height;
    _projectionMatrix = matrix_perspective_right_hand(65.0f * (M_PI / 180.0f), 
                                                      aspect, 
                                                      0.1f, 
                                                      100.0f);
}

matrix_float4x4 matrix_perspective_right_hand(float fovyRadians, 
                                              float aspect, 
                                              float nearZ, 
                                              float farZ) {
    float ys = 1 / tanf(fovyRadians * 0.5);
    float xs = ys / aspect;
    float zs = farZ / (nearZ - farZ);

    return (matrix_float4x4) {{
        { xs,   0,          0,  0 },    // Column 0
        {  0,  ys,          0,  0 },    // Column 1
        {  0,   0,         zs, -1 },    // Column 2
        {  0,   0, nearZ * zs,  0 }     // Column 3
    }};
}
```

Your [`CAMetalLayer`](../QuartzCore/cametallayer.md) views receive a [`UIView`](../UIKit/uiview.md) life cycle call to [`layoutSubviews()`](../UIKit/uiview/layoutsubviews%28%29.md)
and related property updates — [`contentScaleFactor`](../UIKit/uiview/contentscalefactor.md), [`frame`](../UIKit/uiview/frame.md), and [`bounds`](../UIKit/uiview/bounds.md). Use the related properties to update the [`MTLDrawable`](./mtldrawable.md) size by getting the window scene’s [`bounds`](../UIKit/uicoordinatespace/bounds.md) from [`coordinateSpace`](../UIKit/uiwindowscene/geometry/coordinatespace.md) and multiplying it by the [`contentsScale`](../QuartzCore/calayer/contentsscale.md) of your [`CAMetalLayer`](../QuartzCore/cametallayer.md):

**Swift**:

```swift
func resizeDrawable(scaleFactor: CGFloat) {
    var newSize = self.bounds.size
    newSize.width *= scaleFactor
    newSize.height *= scaleFactor

    if newSize.width <= 0 || newSize.height <= 0 {
        return
    }

    if let metalLayer = layer as? CAMetalLayer {
        if newSize.width == metalLayer.drawableSize.width &&
           newSize.height == metalLayer.drawableSize.height {
            return
        }                

        metalLayer.drawableSize = newSize
    }

    delegate?.drawableResize(newSize)
}
```

**Objective-C**:

```objc
- (void)resizeDrawable:(CGFloat)scaleFactor
{
    CGSize newSize = self.bounds.size;
    newSize.width *= scaleFactor;
    newSize.height *= scaleFactor;

    if(newSize.width <= 0 || newSize.width <= 0)
    {
        return;
    }

    if(_metalLayer) {
        if(newSize.width == _metalLayer.drawableSize.width &&
           newSize.height == _metalLayer.drawableSize.height)
        {
            return;
        }

        _metalLayer.drawableSize = newSize;
    } 

    [_delegate drawableResize:newSize];
}
```

#### Handle moving a window between displays

In iPad, you use [`UITraitCollection`](../UIKit/uitraitcollection.md) to assist with providing a flexible windowing environment that allows your app to render and move windows between multiple displays. To eliminate the need to manually register for trait changes, use [Automatic trait tracking](../UIKit/automatic-trait-tracking.md) to observe the values you need from your specific views. In some cases, you might use [`UIScreen`](../UIKit/uiscreen.md) to access a trait that [`UITraitCollection`](../UIKit/uitraitcollection.md) doesn’t provide, like [`nativeScale`](../UIKit/uiscreen/nativescale.md).

When your app’s scene geometry changes — like when moving between screens — the [`UIWindowSceneDelegate`](../UIKit/uiwindowscenedelegate.md) calls the [`windowScene(_:didUpdateEffectiveGeometry:)`](../UIKit/uiwindowscenedelegate/windowscene%28_,didupdateeffectivegeometry%29.md) method to inspect the window geometry and perform necessary updates:

**Swift**:

```swift
func windowScene(
    _ windowScene: UIWindowScene,
    didUpdateEffectiveGeometry previousGeometry: UIWindowScene.Geometry) {

    let geometry = windowScene.effectiveGeometry
    let sceneSize = geometry.coordinateSpace.bounds.size

    // Perform necessary updates after the scene geometry changes.
    if sceneSize != previousSceneSize {
        previousSceneSize = sceneSize
    }
}
```

**Objective-C**:

```objc
- (void)windowScene:(UIWindowScene *)windowScene
        didUpdateEffectiveGeometry:(UIWindowSceneGeometry *)previousGeometry {

    UIWindowSceneGeometry *geometry = windowScene.effectiveGeometry;
    CGSize sceneSize = geometry.coordinateSpace.bounds.size;

    // Perform necessary updates after the scene geometry changes.
    if (!CGSizeEqualToSize(sceneSize, self.previousSceneSize)) {
        self.previousSceneSize = sceneSize;
    }
}
```

For more information on supporting multiple displays in iPadOS, see [Presenting content on a connected display](../UIKit/presenting-content-on-a-connected-display.md). For more information on managing your Metal app window in macOS, see [Managing your game window for Metal in macOS](./managing-your-game-window-for-metal-in-macos.md).

#### Lock interface orientation for device rotation

Some Metal apps and games might need to lock the interface orientation so the screen geometry remains locked when a person rotates the device. To lock the orientation, call [`setNeedsUpdateOfPrefersInterfaceOrientationLocked()`](../UIKit/uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked%28%29.md) in your view controller and check whether the interface is already locked with the `previousEffectiveGeometry` parameter of [`windowScene(_:didUpdateEffectiveGeometry:)`](../UIKit/uiwindowscenedelegate/windowscene%28_,didupdateeffectivegeometry%29.md):

**Swift**:

```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var myGameInstance = MyGame()

    func windowScene(
        _ windowScene: UIWindowScene,
        didUpdateEffectiveGeometry previousGeometry: UIWindowScene.Geometry) {

        let wasLocked = previousGeometry.isInterfaceOrientationLocked
        let isLocked = windowScene.effectiveGeometry.isInterfaceOrientationLocked

        if wasLocked != isLocked {
            myGameInstance.pauseIfNeeded(isInterfaceOrientationLocked: isLocked)
        }
    }
}
```

**Objective-C**:

```objc
- (void)windowScene:(UIWindowScene *)windowScene
        didUpdateEffectiveGeometry:(UIWindowSceneGeometry *)previousGeometry {

    BOOL wasLocked = previousGeometry.interfaceOrientationLocked;
    BOOL isLocked = windowScene.effectiveGeometry.interfaceOrientationLocked;

    if (wasLocked != isLocked) {
        [self.myGameInstance pauseIfNeededWithIsInterfaceOrientationLocked: isLocked];
    }
}
```

For more information on locking your app’s orientation, see [TN3192: Migrating your app from the deprecated UIRequiresFullScreen key](../Technotes/tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md).

## See Also

### Presentation
- [Managing your game window for Metal in macOS](./managing-your-game-window-for-metal-in-macos.md)
  Set up a window and view for optimally displaying your Metal content.
- [Adapting your game interface for smaller screens](./adapting-your-game-interface-for-smaller-screens.md)
  Make text legible on all devices the player chooses to run your game on.
- [Onscreen presentation](./onscreen-presentation.md)
  Show the output from a GPU’s rendering pass to the user in your app.
- [HDR content](./hdr-content.md)
  Take advantage of high dynamic range to present more vibrant colors in your apps and games.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/managing-your-metal-app-window-in-ipados)*