# signatureWithObjCTypes:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an `NSMethodSignature` object for the given Objective-C method type string.

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
+ (NSMethodSignature *) signatureWithObjCTypes:(const char *) types;
```

#### Return Value

An `NSMethodSignature` object for the given Objective-C method type string in `types`.

## Parameters

- `types`: An array of characters containing the type encodings for the method arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmethodsignature/signaturewithobjctypes:)*