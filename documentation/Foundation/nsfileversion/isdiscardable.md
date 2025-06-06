# isDiscardable

**Framework**: Foundation  
**Kind**: property

A Boolean value that specifies whether the system can delete the associated file at some future time.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isDiscardable: Bool { get set }
```

#### Discussion

Marking a file version as discardable gives the system the flexibility to reclaim the space, occupied by the associated file, at some future time. Do not, however, depend on the file being discarded.

After setting this property to [`true`](https://developer.apple.com/documentation/swift/true), do not set this property to [`false`](https://developer.apple.com/documentation/swift/false) again. Doing so causes the system to raise an exception. In addition, if you set this property to [`true`](https://developer.apple.com/documentation/swift/true) for the version of the file returned by the [`currentVersionOfItem(at:)`](nsfileversion/currentversionofitem(at:).md) method, the system raises an exception.

## See Also

- [class func removeOtherVersionsOfItem(at: URL) throws](nsfileversion/removeotherversionsofitem(at:).md)
  Removes all versions of a file, except the current one, from the version store.
- [func remove() throws](nsfileversion/remove.md)
  Remove this version object and its associated file from the version store.
- [var url: URL](nsfileversion/url.md)
  The URL identifying the location of the file associated with the file version object.
- [var localizedName: String?](nsfileversion/localizedname.md)
  The string containing the user-presentable name of the file version.
- [var localizedNameOfSavingComputer: String?](nsfileversion/localizednameofsavingcomputer.md)
  The user-presentable name of the computer on which the revision was saved.
- [var modificationDate: Date?](nsfileversion/modificationdate.md)
  The modification date of the version.
- [var persistentIdentifier: any NSCoding](nsfileversion/persistentidentifier.md)
  The identifier for this version of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/isdiscardable)*