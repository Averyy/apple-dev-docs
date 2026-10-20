# CFDictionaryGetTypeID()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the type identifier for the CFDictionary opaque type.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFDictionaryGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CFDictionaryGetTypeID();
```

#### Return Value

The type identifier for the CFDictionary opaque type.

#### Discussion

CFMutableDictionary objects have the same type identifier as CFDictionary objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarygettypeid())*