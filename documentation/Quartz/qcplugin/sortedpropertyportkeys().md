# sortedPropertyPortKeys()

**Framework**: Quartz  
**Kind**: method  
**Role**: Type Method

Returns and array of property port keys in the order you want them to appear in the user interface.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class func sortedPropertyPortKeys() -> [Any]!
```

```objc
+ (NSArray *) sortedPropertyPortKeys;
```

#### Return Value

The property port keys in the order you want them to appear in the user interface.

#### Discussion

Override this method to specify an optional ordering for property based ports in the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/sortedpropertyportkeys())*