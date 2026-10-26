---
url: "https://docs.swift.org/latest/documentation/packageplugin/package/products(oftype:)"
framework: "Swift-Org/PackagePlugin"
---

# products(ofType:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

The products in this package that conform to a specific type.

## Declaration

```swift
func products<T>(ofType: T.Type) -> [T] where T : Product
```

## See Also

### Inspecting Package Products
- [let products: [Product]](./products.md)
  Any regular products defined in this package, with the exception of plugin products.
- [func products(named: [String]) throws -> [Product]](./products%28named%29.md)
  The list of products matching the given names.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/package/products(oftype:))*