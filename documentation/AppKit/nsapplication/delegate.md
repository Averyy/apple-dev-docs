# delegate

**Framework**: AppKit  
**Kind**: property

The app delegate object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var delegate: (any NSApplicationDelegate)? { get set }
```

#### Discussion

The app object and app delegate work in tandem to manage the app’s overall behavior. Typically, the delegate is configured automatically by the Xcode project templates.

## See Also

- [protocol NSApplicationDelegate](nsapplicationdelegate.md)
  A set of methods that manage your app’s life cycle and its interaction with common system services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/delegate)*