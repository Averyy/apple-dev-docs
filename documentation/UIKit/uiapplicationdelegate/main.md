# main()

**Framework**: UIKit  
**Kind**: method

Provides the top-level entry point for the app.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func main()
```

#### Discussion

[`UIApplicationDelegate`](uiapplicationdelegate.md) provides an implementation of the [`main()`](uiapplicationdelegate/main().md) method so that it can serve as the main entry point for a UIKit app. The system calls the [`main()`](uiapplicationdelegate/main().md) method to launch your app; you never call it yourself. You can have exactly one entry point in your app, which you mark with the `@main` attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/main())*