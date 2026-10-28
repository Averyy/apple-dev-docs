# decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decodes the \c NSDictionary object for the given \c key, which should be an \c NSDictionary<keyCls,objectCls> , with keys of type given in \c keyCls and objects of the given non-collection class \c objectCls (no nested dictionaries or other dictionaries contained in the dictionary, etc) from the coder.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```objc
- (NSDictionary *) decodeDictionaryWithKeysOfClass:(Class) keyCls objectsOfClass:(Class) objectCls forKey:(NSString *) key;
```

## Discussion

Requires \c NSSecureCoding otherwise an exception is thrown and sets the \c decodingFailurePolicy to \c NSDecodingFailurePolicySetErrorAndReturn.

Returns \c nil if the object for \c key is not of the expected types, or cannot be decoded, and sets the \c error on the decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodedictionarywithkeysofclass:objectsofclass:forkey:)*