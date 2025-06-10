# icon

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The pass icon.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@NSCopying
var icon: UIImage { get }
```

#### Discussion

You can use this property to display a pass’s icon as part of a UI element that represents the pass, such as a cell in a table view.

## See Also

- [func localizedValue(forFieldKey: String) -> Any?](pkpass/localizedvalue(forfieldkey:).md)
  Returns the localized value for a specified field of the pass.
- [var organizationName: String](pkpass/organizationname.md)
  The name of the organization that creates the pass.
- [var relevantDate: Date?](pkpass/relevantdate.md)
  The date when the pass is most likely to be useful or necessary.
- [class PKPassRelevantDate](pkpassrelevantdate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/icon)*