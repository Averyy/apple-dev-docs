# suggestedPageSize

**Framework**: File Provider  
**Kind**: property

The page size that the system recommends.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var suggestedPageSize: Int { get }
```

#### Discussion

The system suggests a page size to optimize performance based on the enumeration’s context. The system can request the enumeration of a container for various reasons, such as if the user opens the directory in Finder, opens a file in an application, or if the system needs to materialize the contents of a directory. Each case has its own performance profile.

While using the suggested page size helps ensure the best user experience, the system enforces a maximum of 100 times the suggested size.

## See Also

- [func didEnumerate([any NSFileProviderItemProtocol])](nsfileproviderenumerationobserver/didenumerate(_:).md)
  Provides a batch of enumerated items.
- [func finishEnumerating(upTo: NSFileProviderPage?)](nsfileproviderenumerationobserver/finishenumerating(upto:).md)
  Tells the observer that all of the items have been enumerated up to the specified page.
- [func finishEnumeratingWithError(any Error)](nsfileproviderenumerationobserver/finishenumeratingwitherror(_:).md)
  Tells the observer that an error occurred during item enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderenumerationobserver/suggestedpagesize)*