# relevantDate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The date when the pass is most likely to be useful or necessary.

**Availability**:
- iOS 6.0+ - Deprecated in 18.0
- iPadOS 6.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 2.0+ - Deprecated in 11.0

> **Deprecated**: Use relevantDates

## Declaration

```swift
var relevantDate: Date? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSDate * relevantDate;
```

## Discussion

You can use this property for sorting UI elements that represent passes, such as cells in a table view.

## See Also

### Getting the display attributes
- [var icon: UIImage](./icon.md)
  The pass icon.
- [func localizedValue(forFieldKey: String) -> Any?](./localizedvalue%28forfieldkey%29.md)
  Returns the localized value for a specified field of the pass.
- [var organizationName: String](./organizationname.md)
  The name of the organization that creates the pass.
- [class PKPassRelevantDate](../pkpassrelevantdate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/relevantdate)*