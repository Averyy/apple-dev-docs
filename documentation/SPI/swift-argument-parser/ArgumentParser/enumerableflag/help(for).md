---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/enumerableflag/help(for:)"
framework: "swift-argument-parser/ArgumentParser"
---

# help(for:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method  
**Required**: Yes

Returns the help information to show for the given flag.

## Declaration

```swift
static func help(for value: Self) -> ArgumentHelp?
```

## Discussion

The default implementation for this method always returns `nil`, which groups the flags together with the help provided in the `@Flag` declaration. Implement this method for your custom type to provide different help information for each flag.

## Default Implementations

### EnumerableFlag Implementations
- [static func help(for: Self) -> ArgumentHelp?](./help%28for%29-2qgai.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/enumerableflag/help(for:))*