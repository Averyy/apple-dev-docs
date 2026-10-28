---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argumentarrayparsingstrategy/remaining"
framework: "swift-argument-parser/ArgumentParser"
---

# remaining

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

Parse only unprefixed values from the command-line input, ignoring any inputs that have a dash prefix; this is the default strategy.

## Declaration

```swift
static var remaining: ArgumentArrayParsingStrategy { get }
```

## Discussion

`remaining` is the default parsing strategy for argument arrays.

For example, the `Example` command defined below has a `words` array that uses the `remaining` parsing strategy:

```
@main
struct Example: ParsableCommand {
    @Flag var verbose = false

    @Argument(parsing: .remaining)
    var words: [String]

    func run() {
        print(words.joined(separator: "\n"))
    }
}
```

Any non-dash-prefixed inputs will be captured in the `words` array.

```
$ example --verbose one two
one
two
$ example one two --verbose
one
two
$ example one two --other
Error: Unknown option '--other'
```

If a user uses the `--` terminator in their input, all following inputs will be captured in `words`.

```
$ example one two -- --verbose --other
one
two
--verbose
--other
```

## See Also

### Parsing Strategies
- [static var allUnrecognized: ArgumentArrayParsingStrategy](./allunrecognized.md)
  After parsing, capture all unrecognized inputs in this argument array.
- [static var postTerminator: ArgumentArrayParsingStrategy](./postterminator.md)
  Before parsing arguments, capture all inputs that follow the `--` terminator in this argument array.
- [static var captureForPassthrough: ArgumentArrayParsingStrategy](./captureforpassthrough.md)
  Parse all remaining inputs after parsing any known options or flags, including dash-prefixed inputs and the `--` terminator.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argumentarrayparsingstrategy/remaining)*