# interfaceNames()

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Type Method

Returns the list of BSD names for WLAN interfaces available on the current system.

**Availability**:
- macOS 10.6+ - Deprecated in 10.10

> **Deprecated**: Use the [`CWWiFiClient`](../cwwificlient.md) method [`interfaceNames()`](../cwwificlient/interfacenames%28%29-swift.type.method.md) instead.

## Declaration

```swift
class func interfaceNames() -> Set<String>?
```

```objc
+ (NSSet<NSString *> *) interfaceNames;
```

## Return Value

An NSSet object containing NSString objects representing BSD interface names.

## Discussion

Returns an NSArray of NSString objects representing the supported WLAN BSD interface names avaliable on the current system (i.e. “en1”, “en2”). If there are no supported interfaces for the current system, then this method will return an empty NSArray object. Returns *nil* in the case of an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/interfacenames())*