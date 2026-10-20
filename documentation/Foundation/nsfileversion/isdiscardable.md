# isDiscardable

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether the system can delete the associated file at some future time.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isDiscardable: Bool { get set }
```

```objc
@property (getter=isDiscardable) BOOL discardable;
```

#### Discussion

Marking a file version as discardable gives the system the flexibility to reclaim the space, occupied by the associated file, at some future time. Do not, however, depend on the file being discarded.

After setting this property to [`true`](../../Swift/true.md), do not set this property to [`false`](../../Swift/false.md) again. Doing so causes the system to raise an exception. In addition, if you set this property to [`true`](../../Swift/true.md) for the version of the file returned by the [`currentVersionOfItem(at:)`](./currentversionofitem%28at%29.md) method, the system raises an exception.

## See Also

### Related Documentation
- [class func removeOtherVersionsOfItem(at: URL) throws](./removeotherversionsofitem%28at%29.md)
  Removes all versions of a file, except the current one, from the version store.
- [func remove() throws](./remove%28%29.md)
  Remove this version object and its associated file from the version store.
### Accessing the Version Information
- [var url: URL](./url.md)
  The URL identifying the location of the file associated with the file version object.
- [var localizedName: String?](./localizedname.md)
  The string containing the user-presentable name of the file version.
- [var localizedNameOfSavingComputer: String?](./localizednameofsavingcomputer.md)
  The user-presentable name of the computer on which the revision was saved.
- [var modificationDate: Date?](./modificationdate.md)
  The modification date of the version.
- [var persistentIdentifier: any NSCoding](./persistentidentifier.md)
  The identifier for this version of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/isdiscardable)*