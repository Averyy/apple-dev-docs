# modificationDate

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The modification date of the version.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var modificationDate: Date? { get }
```

```objc
@property (copy, readonly, nullable) NSDate * modificationDate;
```

## Discussion

If the version has been deleted, this value is `nil`.

## See Also

### Accessing the Version Information
- [var url: URL](./url.md)
  The URL identifying the location of the file associated with the file version object.
- [var localizedName: String?](./localizedname.md)
  The string containing the user-presentable name of the file version.
- [var localizedNameOfSavingComputer: String?](./localizednameofsavingcomputer.md)
  The user-presentable name of the computer on which the revision was saved.
- [var persistentIdentifier: any NSCoding](./persistentidentifier.md)
  The identifier for this version of the file.
- [var isDiscardable: Bool](./isdiscardable.md)
  A Boolean value that specifies whether the system can delete the associated file at some future time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/modificationdate)*