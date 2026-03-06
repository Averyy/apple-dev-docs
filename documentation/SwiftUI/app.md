# App

**Framework**: SwiftUI  
**Kind**: protocol

A type that represents the structure and behavior of an app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol App
```

## Mentions

- [Migrating to the SwiftUI life cycle](migrating-to-the-swiftui-life-cycle.md)

#### Overview

Create an app by declaring a structure that conforms to the `App` protocol. Implement the required [`body`](app/body-swift.property.md) computed property to define the app’s content:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            Text("Hello, world!")
        }
    }
}
```

Precede the structure’s declaration with the [`@main`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Attributes.html#ID626) attribute to indicate that your custom `App` protocol conformer provides the entry point into your app. The protocol provides a default implementation of the [`main()`](app/main().md) method that the system calls to launch your app. You can have exactly one entry point among all of your app’s files.

Compose the app’s body from instances that conform to the [`Scene`](scene.md) protocol. Each scene contains the root view of a view hierarchy and has a life cycle managed by the system. SwiftUI provides some concrete scene types to handle common scenarios, like for displaying documents or settings. You can also create custom scenes.

```swift
@main
struct Mail: App {
    var body: some Scene {
        WindowGroup {
            MailViewer()
        }
        Settings {
            SettingsView()
        }
    }
}
```

You can declare state in your app to share across all of its scenes. For example, you can use the [`StateObject`](stateobject.md) attribute to initialize a data model, and then provide that model on a view input as an [`ObservedObject`](observedobject.md) or through the environment as an [`EnvironmentObject`](environmentobject.md) to scenes in the app:

```swift
@main
struct Mail: App {
    @StateObject private var model = MailModel()

    var body: some Scene {
        WindowGroup {
            MailViewer()
                .environmentObject(model) // Passed through the environment.
        }
        Settings {
            SettingsView(model: model) // Passed as an observed object.
        }
    }
}
```

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Implementing an app
- [var body: Self.Body](app/body-swift.property.md)
  The content and behavior of the app.
- [associatedtype Body : Scene](app/body-swift.associatedtype.md)
  The type of scene representing the content of the app.
### Running an app
- [init()](app/init.md)
  Creates an instance of the app using the body that you define for its content.
- [static func main()](app/main.md)
  Initializes and runs the app.

## See Also

- [Destination Video](../visionOS/destination-video.md)
  Leverage SwiftUI to build an immersive media experience in a multiplatform app.
- [Hello World](../visionOS/World.md)
  Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Backyard Birds: Building an app with SwiftData and widgets](backyard-birds-sample.md)
  Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.
- [Food Truck: Building a SwiftUI multiplatform app](food-truck-building-a-swiftui-multiplatform-app.md)
  Create a single codebase and app target for Mac, iPad, and iPhone.
- [Fruta: Building a feature-rich app with SwiftUI](../AppClip/fruta-building-a-feature-rich-app-with-swiftui.md)
  Create a shared codebase to build a multiplatform app that offers widgets and an App Clip.
- [Migrating to the SwiftUI life cycle](migrating-to-the-swiftui-life-cycle.md)
  Use a scene-based life cycle in SwiftUI while keeping your existing codebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/app)*