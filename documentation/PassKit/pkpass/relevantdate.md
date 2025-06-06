# relevantDate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The date when the pass is most likely to be useful or necessary.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var relevantDate: Date? { get }
```

#### Discussion

You can use this property for sorting UI elements that represent passes, such as cells in a table view.

## See Also

- [var icon: UIImage](pkpass/icon.md)
  The pass icon.
- [func localizedValue(forFieldKey: String) -> Any?](pkpass/localizedvalue(forfieldkey:).md)
  Returns the localized value for a specified field of the pass.
- [var organizationName: String](pkpass/organizationname.md)
  The name of the organization that creates the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/relevantdate)*