# SSReadingList

**Framework**: Safari Services  
**Kind**: class  
**Role**: Class

An object for adding items to a user’s Safari Reading List.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class SSReadingList
```

```objc
@interface SSReadingList : NSObject
```

## Topics

### Getting the Reading List Singleton Object
- [class func `default`() -> SSReadingList?](./ssreadinglist/default%28%29.md)
  Returns the Safari Reading List singleton object.
### Checking Whether a URL is Supported by Reading List
- [class func supportsURL(URL) -> Bool](./ssreadinglist/supportsurl%28_%29.md)
  Determines whether a URL can be added to the Reading List.
### Adding an Item to the Reading List
- [func addItem(with: URL, title: String?, previewText: String?) throws](./ssreadinglist/additem%28with,title,previewtext%29.md)
  Adds an item to the Reading List.
### Constants
- [Reading List Error Domain](./reading-list-error-domain.md)
  The domain used for Reading List errors.
- [SSReadingListError.Code](./ssreadinglisterror/code.md)
  Messages that describe a Safari Reading List error.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Safari Reading List
- [let SSReadingListErrorDomain: String](./ssreadinglisterrordomain.md)
  The domain for Safari Reading List errors.
- [SSReadingListError.Code](./ssreadinglisterror/code.md)
  Messages that describe a Safari Reading List error.
- [struct SSReadingListError](./ssreadinglisterror.md)
  A Safari Reading List error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/ssreadinglist)*