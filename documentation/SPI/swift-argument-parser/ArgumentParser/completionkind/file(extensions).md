---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionkind/file(extensions:)"
framework: "swift-argument-parser/ArgumentParser"
---

# file(extensions:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

The completion candidates include directory and file names, the latter filtered by the given list of extensions.

## Declaration

```swift
static func file(extensions: [String] = []) -> CompletionKind
```

#### Discussion

If the given list of extensions is empty, then file names are not filtered.

Given file extensions must not include the `.` initial extension separator.

Given file extensions are parsed by the requesting shell as globs; Swift Argument Parser does not perform any escaping or quoting.

The directory/file filter and the given list of extensions are included in a completion script when it is generated.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionkind/file(extensions:))*