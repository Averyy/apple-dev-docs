# actions

**Framework**: TipKit  
**Kind**: property  
**Required**: Yes

Buttons that help people get started or learn more about your feature.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@Tips
.ActionBuilder var actions: [Self.Action] { get }
```

#### Discussion

Use actions to provide primary and secondary buttons to help people get started or learn more about your feature. If you don’t supply a value, this property returns an empty array of type `Action`.

## See Also

- [typealias Action](tip/action.md)
  A type that describes a control associated with a tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tip/actions)*