# kIOPropertyCylinderCountKey

**Framework**: DriverKit  
**Kind**: macro

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
#define kIOPropertyCylinderCountKey
```

#### Discussion

This key is used to define the number of heads for a particular medium.

Requirement: Mandatory element of the Rigid Disk Geometry dictionary.

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
   	<key>Rigid Disk Geometry</key>
   	<dict>
   		<key>Sector Count per Track</key>
   		<integer>12345</integer>
   		<key>Head Count</key>
   		<integer>12</integer>
   		<key>Cylinder Count</key>
   		<integer>12345</integer>
   		<key>Bytes per Physical Sector</key>
   		<integer>512</integer>
   	</dict>
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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/kiopropertycylindercountkey)*