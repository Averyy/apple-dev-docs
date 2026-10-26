# title

**Framework**: SharedWithYouCore  
**Kind**: property  
**Role**: Instance Property

A localized string the system displays as a title to represent the permissions option.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var title: String { get set }
```

```objc
@property (nonatomic, copy) NSString * title;
```

## See Also

### Accessing option attributes
- [var identifier: String](./identifier.md)
  A unique identifier.
- [var isSelected: Bool](./isselected.md)
  A Boolean value that represents the selected state of an option.
- [var requiredOptionsIdentifiers: [String]](./requiredoptionsidentifiers.md)
  An array of option identifiers that the app must select before the system makes the option interactive.
- [var subtitle: String](./subtitle.md)
  A localized string the system displays to represent the permissions option in the collaboration view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationoption/title)*