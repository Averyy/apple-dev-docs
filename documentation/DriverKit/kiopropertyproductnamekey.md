# kIOPropertyProductNameKey

**Framework**: DriverKit  
**Kind**: macro

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
#define kIOPropertyProductNameKey
```

#### Discussion

This key is used to define the Product Name for a particular device and it has an associated string.

Requirement: Mandatory

Example:

```objc
 
 
<dict>
   <key>Device Characteristics</key>
   <dict>
   	<key>Vendor Name</key>
   	<string>Apple</string>
   	<key>Product Name</key>
   	<string>iPod</string>
   	<key>Product Revision Level</key>
   	<string>1.0</string>
   </dict>
</dict>
```

## See Also

- [ALWAYS](always.md)
- [APPLE_KEXT_OVERRIDE](apple_kext_override.md)
- [DEFN](defn.md)
- [DRIVERKIT_CONSUMED](driverkit_consumed.md)
- [DRIVERKIT_CONSUMES_THIS](driverkit_consumes_this.md)
- [DRIVERKIT_FRAMEWORK_INCLUDE](driverkit_framework_include.md)
- [DRIVERKIT_IOLIB_H](driverkit_iolib_h.md)
- [DRIVERKIT_OSCOLLECTIONS_H](driverkit_oscollections_h.md)
- [DRIVERKIT_RETURNS_NOT_RETAINED](driverkit_returns_not_retained.md)
- [DRIVERKIT_RETURNS_RETAINED](driverkit_returns_retained.md)
- [DRIVERKIT_RETURNS_RETAINED_ON_NONZERO](driverkit_returns_retained_on_nonzero.md)
- [DRIVERKIT_RETURNS_RETAINED_ON_ZERO](driverkit_returns_retained_on_zero.md)
- [ERR_SUCCESS](err_success.md)
- [EXTENDS](extends.md)
- [HIDDEN](hidden.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/kiopropertyproductnamekey)*