# userInfo()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a mutable dictionary for storing arbitrary information.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func userInfo() -> NSMutableDictionary!
```

```objc
- (NSMutableDictionary *) userInfo;
```

#### Return Value

A mutable dictionary.

#### Discussion

The `userInfo` dictionary is shared—there is one per Quartz Composer context. In fact, it is the same dictionary as the one available for the plug-in execution context for instances of the [`QCPlugIn`](../qcplugin.md) class.

When you add information to the dictionary, make sure that you use unique keys, such as `“com.myCompany.foo”`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrenderer/userinfo())*