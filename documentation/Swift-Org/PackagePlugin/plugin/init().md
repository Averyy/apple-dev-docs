---
url: "https://docs.swift.org/latest/documentation/packageplugin/plugin/init()"
framework: "Swift-Org/PackagePlugin"
---

# init()

**Framework**: Swift-Org/PackagePlugin  
**Kind**: init  
**Role**: Initializer  
**Required**: Yes

Instantiates the plugin.

## Declaration

```swift
init()
```

#### Discussion

This happens once per invocation of the plugin. There is no facility for keeping in-memory state from one invocation to the next. Most plugins do not need to implement the initializer.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/plugin/init())*