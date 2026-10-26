# requiredOptionsIdentifiers

**Framework**: SharedWithYouCore  
**Kind**: property  
**Role**: Instance Property

An array of option identifiers that the app must select before the system makes the option interactive.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var requiredOptionsIdentifiers: [String] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSString *> * requiredOptionsIdentifiers;
```

## See Also

### Accessing option attributes
- [var identifier: String](./identifier.md)
  A unique identifier.
- [var isSelected: Bool](./isselected.md)
  A Boolean value that represents the selected state of an option.
- [var subtitle: String](./subtitle.md)
  A localized string the system displays to represent the permissions option in the collaboration view.
- [var title: String](./title.md)
  A localized string the system displays as a title to represent the permissions option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationoption/requiredoptionsidentifiers)*