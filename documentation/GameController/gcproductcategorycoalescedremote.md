# GCProductCategoryCoalescedRemote

**Framework**: Game Controller  
**Kind**: var

The Apple TV Remote product category for physical and virtual remotes that Game Center combines into a single device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
let GCProductCategoryCoalescedRemote: String
```

#### Discussion

Game Controller merges the physical Apple TV Remote with the virtual Apple TV Remote app into one [`GCDevice`](gcdevice.md) object by default. To disable this behavior, or if you fully support the second-generation Siri Remote, set the [`GCSupportsMultipleMicroGamepads`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GCSupportsMultipleMicroGamepads) key to `YES` in the information property list.

## See Also

- [let GCProductCategorySiriRemote1stGen: String](gcproductcategorysiriremote1stgen.md)
  The first-generation Siri Remote or first-generation Apple TV Remote product category.
- [let GCProductCategorySiriRemote2ndGen: String](gcproductcategorysiriremote2ndgen.md)
  The second-generation Siri Remote or second-generation Apple TV Remote product category.
- [let GCProductCategoryControlCenterRemote: String](gcproductcategorycontrolcenterremote.md)
  The virtual remote in the Control Center on iOS and tvOS devices for controlling the Apple TV.
- [let GCProductCategoryUniversalElectronicsRemote: String](gcproductcategoryuniversalelectronicsremote.md)
  The product category for a Universal Electronics remote that works with Apple TV.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcproductcategorycoalescedremote)*