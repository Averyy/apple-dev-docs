# plugInKeys()

**Framework**: Quartz  
**Kind**: method

Returns the keys for the internal settings of a custom patch.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func plugInKeys() -> [Any]!
```

#### Return Value

An array of keys used for key-value coding (KVC) of the internal settings.

#### Discussion

You must override this method if your patch provides a Settings pane.  This keys are used for automatic serialization of the internal settings and are also used by the [`QCPlugInViewController`](qcpluginviewcontroller.md) instance for the Settings pane. The implementation is straightforward; the keys are strings that represent the instance variables used for the Settings pane. For example, the `plugInKeys` method for these instance variables:

```objc
@property(ivar, byref) NSColor * systemColor;
@property(ivar, byref) NSConfiguration * systemConfiguration;
```

are:

```objc
+ (NSArray*) plugInKeys
{
    return [NSArray arrayWithObjects: @"systemColor",
                                      @"systemConfiguration",
                                      nil];
}
```

## See Also

- [func createViewController() -> QCPlugInViewController!](qcplugin/createviewcontroller.md)
  Creates and returns a view controller for the Settings pane of a custom patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/pluginkeys())*