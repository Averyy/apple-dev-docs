# automatic

**Framework**: SwiftUI  
**Kind**: property

The automatic activation of the scope bar.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
static var automatic: SearchScopeActivation { get }
```

#### Discussion

By default, this is [`onTextEntry`](searchscopeactivation/ontextentry.md) in iOS and [`onSearchPresentation`](searchscopeactivation/onsearchpresentation.md) in macOS.

## See Also

- [static var onSearchPresentation: SearchScopeActivation](searchscopeactivation/onsearchpresentation.md)
  An activation where the system shows search scopes after presenting search and hides search scopes after search cancellation.
- [static var onTextEntry: SearchScopeActivation](searchscopeactivation/ontextentry.md)
  An activation where the system shows search scopes when typing begins in the search field and hides search scopes after search cancellation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/searchscopeactivation/automatic)*