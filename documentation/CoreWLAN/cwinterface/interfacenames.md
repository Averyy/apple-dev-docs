# interfaceNames()

**Framework**: Core WLAN  
**Kind**: method

Returns the list of BSD names for WLAN interfaces available on the current system.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class func interfaceNames() -> Set<String>?
```

#### Return Value

An NSSet object containing NSString objects representing BSD interface names.

#### Discussion

Returns an NSArray of NSString objects representing the supported WLAN BSD interface names avaliable on the current system (i.e. “en1”, “en2”). If there are no supported interfaces for the current system, then this method will return an empty NSArray object. Returns  in the case of an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/interfacenames())*