---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandconfiguration/discussion"
framework: "swift-argument-parser/ArgumentParser"
---

# discussion

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Instance Property

A longer description of this command, to be shown in the extended help display.

## Declaration

```swift
var discussion: String
```

#### Discussion

Can include specific abstracts about the argument’s possible values (e.g. for a custom `ExpressibleByArgument` type), or can describe a static block of text that extends the description of the argument.

## See Also

### Customizing the Help Screen
- [var abstract: String](./abstract.md)
  A one-line description of this command.
- [var usage: String?](./usage.md)
  A customized usage string to be shown in the help display and error messages.
- [var helpBanner: String?](./helpbanner.md)
  A banner shown at the top of the help display for this command and, unless overridden, all of its subcommands.
- [var helpNames: NameSpecification?](./helpnames.md)
  Flag names to be used for help.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandconfiguration/discussion)*