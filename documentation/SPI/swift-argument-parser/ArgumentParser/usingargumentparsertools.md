---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/usingargumentparsertools"
framework: "swift-argument-parser/ArgumentParser"
---

# Using ArgumentParser Tools

**Framework**: swift-argument-parser/ArgumentParser  
**Role**: Article

Learn how to provide input to command-line tools built with `ArgumentParser`.

## Overview

Tools built with `ArgumentParser` can accept positional arguments, named options, and flags. The tool’s help screen describes the inputs it supports; run a tool with the `--help` flag to display it.

### Separating Options from Positional Arguments

Use the `--` option terminator when a positional value starts with a dash and could otherwise be interpreted as an option or flag. A tool stops recognizing options and flags after `--` and treats every remaining input as positional. The terminator itself isn’t included in the parsed values:

```
% example --verbose -- file1.swift file2.swift --other
Verbose: true, files: ["file1.swift", "file2.swift", "--other"]
```

This convention also lets you pass a positional value that has the same spelling as a declared option or flag. In the following example, `--verbose` is stored in `files` instead of setting the `verbose` flag:

```
% example -- --verbose file1.swift
Verbose: false, files: ["--verbose", "file1.swift"]
```

## See Also

### Essentials
- [Getting Started with ArgumentParser](./gettingstarted.md)
  Learn to set up and customize a simple command-line tool.
- [protocol ParsableCommand](./parsablecommand.md)
  A type that can be executed as part of a nested tree of commands.
- [protocol AsyncParsableCommand](./asyncparsablecommand.md)
  A type that can be executed asynchronously, as part of a nested tree of commands.
- [Defining Commands and Subcommands](./commandsandsubcommands.md)
  Break complex command-line tools into a tree of subcommands.
- [Customizing Help for Commands](./customizingcommandhelp.md)
  Define your command’s abstract, extended discussion, or usage string, and set the flags used to invoke the help display.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/usingargumentparsertools)*