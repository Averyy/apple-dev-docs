# body

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The content and behavior of the app.

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
@SceneBuilder
@MainActor @preconcurrency var body: Self.Body { get }
```

## Discussion

For any app that you create, provide a computed `body` property that defines your app’s scenes, which are instances that conform to the [`Scene`](../scene.md) protocol. For example, you can create a simple app with a single scene containing a single view:

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

Swift infers the app’s [`Body`](./body-swift.associatedtype.md) associated type based on the scene provided by the `body` property.

## See Also

### Implementing an app
- [associatedtype Body : Scene](./body-swift.associatedtype.md)
  The type of scene representing the content of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/app/body-swift.property)*