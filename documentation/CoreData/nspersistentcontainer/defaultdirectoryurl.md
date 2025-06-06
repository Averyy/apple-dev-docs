# defaultDirectoryURL()

**Framework**: Core Data  
**Kind**: method

Returns the location of the directory that contains the persistent stores.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func defaultDirectoryURL() -> URL
```

#### Return Value

An [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) that references the directory in which the persistent store(s) will be located or are currently located.

#### Discussion

This method returns a platform-dependent [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) at which the persistent store(s) will be located or are currently located. This method can be overridden in a subclass of [`NSPersistentContainer`](nspersistentcontainer.md).

## See Also

- [class var defaultDirectoryURL: URL](nspersistentcontainer/defaultdirectoryurl-swift.type.property.md)
  The location of the directory that contains the persistent stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/defaultdirectoryurl())*