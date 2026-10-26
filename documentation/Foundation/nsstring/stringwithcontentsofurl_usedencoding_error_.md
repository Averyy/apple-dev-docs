# stringWithContentsOfURL:usedEncoding:error:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a string created by reading data from the file at a given URL and returns by reference the encoding used to interpret the data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) stringWithContentsOfURL:(NSURL *) url usedEncoding:(NSStringEncoding *) enc error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/stringwithcontentsofurl:usedencoding:error:)*