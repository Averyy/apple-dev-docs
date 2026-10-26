---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/enumerableflag/help(for:)-2qgai"
framework: "swift-argument-parser/ArgumentParser"
---

# help(for:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Returns the help information to show for the given flag.

## Declaration

```swift
static func help(for value: Self) -> ArgumentHelp?
```

#### Discussion

The default implementation for this method always returns `nil`, which groups the flags together with the help provided in the `@Flag` declaration. Implement this method for your custom type to provide different help information for each flag.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/enumerableflag/help(for:)-2qgai)*