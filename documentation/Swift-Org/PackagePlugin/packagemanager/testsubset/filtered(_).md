---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testsubset/filtered(_:)"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.TestSubset.filtered(_:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: case  
**Role**: Case

One or more tests filtered by regular expression. Use the format `<test-target>.<test-case>` or `<test-target>.<test-case>/<test>`.

## Declaration

```swift
case filtered([String])
```

## Discussion

This is the same as the `--filter` option of `swift test`.

## See Also

### Subsets of Tests
- [PackageManager.TestSubset.all](./all.md)
  All tests in the package.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testsubset/filtered(_:))*