# CFBridgingRelease

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Moves a non-Objective-C pointer to Objective-C and also transfers ownership to ARC.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
static idCFBridgingRelease(CFTypeRef X);
```

#### Discussion

You use this function to cast a Core Foundation-style object as an Objective-C object and transfer ownership of the object to ARC such that you don’t have to release the object, as illustrated in this example:

```objc
CFStringRef cfName = ABRecordCopyValue(person, kABPersonFirstNameProperty);
NSString *name = (NSString *)CFBridgingRelease(cfName);
```

## See Also

### Core Foundation ARC Integration
- [func CFBridgingRetain(Any?) -> CFTypeRef?](./cfbridgingretain%28_%29.md)
  Casts an Objective-C pointer to a Core Foundation pointer and also transfers ownership to the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/cfbridgingrelease)*