# localizedName

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The string containing the user-presentable name of the file version.

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
var localizedName: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * localizedName;
```

#### Discussion

When displaying different versions of a file to the user, you should present this string to the user instead of the version’s URL.

## See Also

### Accessing the Version Information
- [var url: URL](./url.md)
  The URL identifying the location of the file associated with the file version object.
- [var localizedNameOfSavingComputer: String?](./localizednameofsavingcomputer.md)
  The user-presentable name of the computer on which the revision was saved.
- [var modificationDate: Date?](./modificationdate.md)
  The modification date of the version.
- [var persistentIdentifier: any NSCoding](./persistentidentifier.md)
  The identifier for this version of the file.
- [var isDiscardable: Bool](./isdiscardable.md)
  A Boolean value that specifies whether the system can delete the associated file at some future time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/localizedname)*