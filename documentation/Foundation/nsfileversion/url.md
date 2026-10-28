# url

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The URL identifying the location of the file associated with the file version object.

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
var url: URL { get }
```

```objc
@property (copy, readonly) NSURL * URL;
```

## Discussion

The URL identifies the location of the file associated with this version. If this version of the file has been deleted, the value in this property is `nil`.

Do not display any part of this URL to the user. The location of file versions is managed by the system and should not be exposed to the user. If you want to present the name of a file version, use the [`localizedName`](./localizedname.md) property.

## See Also

### Accessing the Version Information
- [var localizedName: String?](./localizedname.md)
  The string containing the user-presentable name of the file version.
- [var localizedNameOfSavingComputer: String?](./localizednameofsavingcomputer.md)
  The user-presentable name of the computer on which the revision was saved.
- [var modificationDate: Date?](./modificationdate.md)
  The modification date of the version.
- [var persistentIdentifier: any NSCoding](./persistentidentifier.md)
  The identifier for this version of the file.
- [var isDiscardable: Bool](./isdiscardable.md)
  A Boolean value that specifies whether the system can delete the associated file at some future time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/url)*