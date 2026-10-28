# icon

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The pass icon.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
@NSCopying
var icon: UIImage { get }
```

```objc
@property (nonatomic, copy, readonly) UIImage * icon;
```

## Discussion

You can use this property to display a pass’s icon as part of a UI element that represents the pass, such as a cell in a table view.

## See Also

### Getting the display attributes
- [func localizedValue(forFieldKey: String) -> Any?](./localizedvalue%28forfieldkey%29.md)
  Returns the localized value for a specified field of the pass.
- [var organizationName: String](./organizationname.md)
  The name of the organization that creates the pass.
- [var relevantDate: Date?](./relevantdate.md)
  The date when the pass is most likely to be useful or necessary.
- [class PKPassRelevantDate](../pkpassrelevantdate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/icon)*