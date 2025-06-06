# organizationName

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The name of the organization that creates the pass.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var organizationName: String { get }
```

#### Discussion

You can use this property to display information about the organization that creates the pass as part of a user interface element that represents the pass, such as a cell in a table view.

## See Also

- [var icon: UIImage](pkpass/icon.md)
  The pass icon.
- [func localizedValue(forFieldKey: String) -> Any?](pkpass/localizedvalue(forfieldkey:).md)
  Returns the localized value for a specified field of the pass.
- [var relevantDate: Date?](pkpass/relevantdate.md)
  The date when the pass is most likely to be useful or necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/organizationname)*