# defaultDirectoryURL()

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSURL *) defaultDirectoryURL;
```

## Return Value

An [`NSURL`](../../Foundation/nsurl.md) that references the directory in which the persistent store(s) will be located or are currently located.

## Discussion

This method returns a platform-dependent [`NSURL`](../../Foundation/nsurl.md) at which the persistent store(s) will be located or are currently located. This method can be overridden in a subclass of [`NSPersistentContainer`](../nspersistentcontainer.md).

## See Also

### Accessing the Default Directory
- [class var defaultDirectoryURL: URL](./defaultdirectoryurl-swift.type.property.md)
  The location of the directory that contains the persistent stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/defaultdirectoryurl())*