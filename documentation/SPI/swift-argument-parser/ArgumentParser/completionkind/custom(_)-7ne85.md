---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionkind/custom(_:)-7ne85"
framework: "swift-argument-parser/ArgumentParser"
---

# custom(_:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

The completion candidates are the strings in the array returned by the given closure when it is executed in response to a user’s request for completions.

## Declaration

```swift
@preconcurrency
static func custom(_ completion: @Sendable @escaping ([String], Int, String) -> [String]) -> CompletionKind
```

## Discussion

Completion candidates are interpreted by the requesting shell as literals. They must be neither escaped nor quoted; Swift Argument Parser escapes or quotes them as necessary for the requesting shell.

The given closure is evaluated after a user invokes completion in their shell (normally by pressing TAB); it is not evaluated when a completion script is generated.

The array of strings passed to the given closure contains all the shell words in the command line for the current command at completion invocation; this is exclusive of words for prior or subsequent commands or pipes, but inclusive of redirects and any other command line elements. Each word is its own element in the argument array; they appear in the same order as in the command line. Note that shell words may contain spaces if they are escaped or quoted.

Shell words are passed to Swift verbatim, without processing or removing any quotes or escapes. For example, the shell word `"abc\\""def"` would be passed to Swift as `"abc\\""def"` (i.e. the Swift String’s contents would include all 4 of the double quotes and the 2 consecutive backslashes).

The second argument (an `Int`) is the 0-based index of the word for which completions are being requested within the given `[String]`.

The third argument (a `String`) is the prefix of the word for which completions are being requested that precedes the cursor.

### bash

In bash 3-, a process substitution (`<(…)`) in the command line prevents Swift custom completion functions from being called.

In bash 4+, a process substitution (`<(…)`) is split into multiple elements in the argument array: one for the starting `<(`, and one for each unescaped/unquoted-space-separated token through the closing `)`.

In bash, if the cursor is between the backslash and the single quote for the last escaped single quote in a word, all subsequent pipes or other commands are included in the words passed to Swift. This oddity might occur only when additional constraints are met. This or similar oddities might occur in other circumstances.

### fish

In fish 3-, due to a bug, the argument array includes the fish words only through the word being completed. This is fixed in fish 4+.

In fish, a redirect’s symbol is not included, but its source/target is.

In fish 3-, due to limitations, words are passed to Swift unquoted. For example, the shell word `"abc\\""def"` would be passed to Swift as `abc\def`. This is fixed in fish 4+.

In fish 3-, the cursor index is provided based on the verbatim word, not based on the unquoted word, so it can be inconsistent with the unquoted word that is supplied to Swift. This problem does not exist in fish 4+.

### zsh

In zsh, redirects (both their symbol and source/target) are omitted.

In zsh, if the cursor is between a backslash and the character that it escapes, the shell cursor index will be indicated as after the escaped character, not as after the backslash.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionkind/custom(_:)-7ne85)*