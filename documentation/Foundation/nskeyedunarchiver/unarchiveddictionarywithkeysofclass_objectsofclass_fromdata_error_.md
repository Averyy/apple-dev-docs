# unarchivedDictionaryWithKeysOfClass:objectsOfClass:fromData:error:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Decodes the \c NSDictionary root object from \c data which should be an \c NSDictionary<keyCls,objectCls>  with keys of type given in \c keyCls and objects of the given non-collection class \c objectCls (no nested dictionaries or other dictionaries contained in the dictionary, etc) from the given archive, previously encoded by \c NSKeyedArchiver.

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
+ (NSDictionary *) unarchivedDictionaryWithKeysOfClass:(Class) keyCls objectsOfClass:(Class) valueCls fromData:(NSData *) data error:(NSError **) error;
```

#### Discussion

Enables \c requiresSecureCoding and sets the \c decodingFailurePolicy to \c NSDecodingFailurePolicySetErrorAndReturn.

Returns \c nil if the given data is not valid or cannot be decoded, and sets the \c error out parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/unarchiveddictionarywithkeysofclass:objectsofclass:fromdata:error:)*