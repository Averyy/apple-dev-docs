---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argumentarrayparsingstrategy/captureforpassthrough"
framework: "swift-argument-parser/ArgumentParser"
---

# captureForPassthrough

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

Parse all remaining inputs after parsing any known options or flags, including dash-prefixed inputs and the `--` terminator.

## Declaration

```swift
static var captureForPassthrough: ArgumentArrayParsingStrategy { get }
```

## Discussion

You can use the `captureForPassthrough` parsing strategy if you need to capture a user’s input to manually pass it unchanged to another command.

When you use this parsing strategy, the parser stops parsing flags and options as soon as it encounters a positional argument or an unrecognized flag, and captures all remaining inputs in the array argument.

For example, the `Example` command defined below has an `words` array that uses the `captureForPassthrough` parsing strategy:

```
@main
struct Example: ParsableCommand {
    @Flag var verbose = false

    @Argument(parsing: .captureForPassthrough)
    var words: [String] = []

    func run() {
        print(words.joined(separator: "\n"))
    }
}
```

Any values after the first unrecognized input are captured in the `words` array.

```
$ example --verbose one two --other
one
two
--other
$ example one two --verbose
one
two
--verbose
```

With the `captureForPassthrough` parsing strategy, the `--` terminator is included in the captured values.

```
$ example --verbose one two -- --other
one
two
--
--other
```

> **Note**: This parsing strategy can be surprising for users, particularly when combined with options and flags. Prefer [`remaining`](./remaining.md) or [`allUnrecognized`](./allunrecognized.md) whenever possible, since users can always terminate options and flags with the `--` terminator. With the `remaining` parsing strategy, the input `--verbose -- one two --other` would have the same result as the first example above.

## See Also

### Parsing Strategies
- [static var remaining: ArgumentArrayParsingStrategy](./remaining.md)
  Parse only unprefixed values from the command-line input, ignoring any inputs that have a dash prefix; this is the default strategy.
- [static var allUnrecognized: ArgumentArrayParsingStrategy](./allunrecognized.md)
  After parsing, capture all unrecognized inputs in this argument array.
- [static var postTerminator: ArgumentArrayParsingStrategy](./postterminator.md)
  Before parsing arguments, capture all inputs that follow the `--` terminator in this argument array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argumentarrayparsingstrategy/captureforpassthrough)*