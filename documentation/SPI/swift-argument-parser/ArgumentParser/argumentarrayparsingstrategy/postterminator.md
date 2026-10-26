---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argumentarrayparsingstrategy/postterminator"
framework: "swift-argument-parser/ArgumentParser"
---

# postTerminator

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

Before parsing arguments, capture all inputs that follow the `--` terminator in this argument array.

## Declaration

```swift
static var postTerminator: ArgumentArrayParsingStrategy { get }
```

#### Discussion

For example, the `Example` command defined below has a `words` array that uses the `postTerminator` parsing strategy:

```
@main
struct Example: ParsableCommand {
    @Flag var verbose = false
    @Argument var name = ""

    @Argument(parsing: .postTerminator)
    var words: [String]

    func run() {
        print(words.joined(separator: "\n"))
    }
}
```

Before looking for the `--verbose` flag and `<name>` argument, any inputs after the `--` terminator are captured into the `words` array.

```
$ example --verbose Asa -- one two --other
one
two
--other
$ example Asa Extra -- one two --other
Error: Unexpected argument 'Extra'
```

Because options are parsed before arguments, an option that consumes or suppresses the `--` terminator can prevent a `postTerminator` argument array from capturing any input. In particular, the [`unconditional`](../singlevalueparsingstrategy/unconditional.md), [`unconditionalSingleValue`](../arrayparsingstrategy/unconditionalsinglevalue.md), and [`remaining`](../arrayparsingstrategy/remaining.md) parsing strategies can all consume the terminator as part of their values.

> **Note**: This parsing strategy can be surprising for users, since it changes the behavior of the `--` terminator. Prefer [`remaining`](./remaining.md) whenever possible.

## See Also

### Parsing Strategies
- [static var remaining: ArgumentArrayParsingStrategy](./remaining.md)
  Parse only unprefixed values from the command-line input, ignoring any inputs that have a dash prefix; this is the default strategy.
- [static var allUnrecognized: ArgumentArrayParsingStrategy](./allunrecognized.md)
  After parsing, capture all unrecognized inputs in this argument array.
- [static var captureForPassthrough: ArgumentArrayParsingStrategy](./captureforpassthrough.md)
  Parse all remaining inputs after parsing any known options or flags, including dash-prefixed inputs and the `--` terminator.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argumentarrayparsingstrategy/postterminator)*