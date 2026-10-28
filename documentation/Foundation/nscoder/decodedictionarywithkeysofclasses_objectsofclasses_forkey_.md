# decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decodes the \c NSDictionary object for the given \c key, which should be an \c NSDictionary, with keys of the types given in \c keyClasses and objects of the given non-collection classes in \c objectClasses (no nested dictionaries or other dictionaries contained in the dictionary, etc) from the given coder.

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
- (NSDictionary *) decodeDictionaryWithKeysOfClasses:(NSSet<Class> *) keyClasses objectsOfClasses:(NSSet<Class> *) objectClasses forKey:(NSString *) key;
```

## Discussion

Requires \c NSSecureCoding otherwise an exception is thrown and sets the \c decodingFailurePolicy to \c NSDecodingFailurePolicySetErrorAndReturn.

Returns \c nil if the object for \c key is not of the expected types, or cannot be decoded, and sets the \c error on the decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodedictionarywithkeysofclasses:objectsofclasses:forkey:)*