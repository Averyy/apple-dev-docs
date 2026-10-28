---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandconfiguration/helpbanner"
framework: "swift-argument-parser/ArgumentParser"
---

# helpBanner

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Instance Property

A banner shown at the top of the help display for this command and, unless overridden, all of its subcommands.

## Declaration

```swift
var helpBanner: String?
```

## Discussion

If `helpBanner` is `nil`, the banner is inherited from the nearest ancestor command that specifies one. To suppress an inherited banner, set `helpBanner` to the empty string. Unlike `abstract` and `discussion`, a banner is printed verbatim and is never wrapped to the terminal width.

## See Also

### Customizing the Help Screen
- [var abstract: String](./abstract.md)
  A one-line description of this command.
- [var discussion: String](./discussion.md)
  A longer description of this command, to be shown in the extended help display.
- [var usage: String?](./usage.md)
  A customized usage string to be shown in the help display and error messages.
- [var helpNames: NameSpecification?](./helpnames.md)
  Flag names to be used for help.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandconfiguration/helpbanner)*