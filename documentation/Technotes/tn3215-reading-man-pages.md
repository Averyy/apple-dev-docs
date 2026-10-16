# TN3215: Reading man pages

**Framework**: Technotes

Use the Terminal app to read the documentation for command-line tools and low-level APIs.

#### Overview

Apple’s man pages, short for *manual pages*, document command-line tools, low-level APIs, and file formats.  If you’re working at the lowest levels of the system, don’t miss out on this rich source of information.

#### Display a Man Page in the Terminal App

Type `man` and the name of a tool or API whose documentation you want to access, and press Return.  Because the man page is larger than the window, Terminal displays only the first part of the page.  Press Space to display subsequent parts, or press Q to exit the `man` tool.

> ❗ **Important**: Developer-oriented man pages are distributed as part of Xcode.  The `man` tool searches for man pages within the active developer directory.  If you have multiple copies of Xcode installed, select your active developer directory using the `xcode-select` command-line tool.  See the `xcode-select` man page for details.

#### Search a Specific Section

Section 1 of the man pages covers command-line tools, section 2 covers system calls, section 3 covers user-space libraries, and so on.  If you don’t specify a section, `man` displays the page from the first section that has a matching entry.  For example, the following command displays the man page for the `open` command-line tool:

```None
% man open
```

To get the man page for the `open` system call, specify section 2:

```None
% man 2 open
```

If you’re not sure which section to use, do a keyword search using the `-k` option.  For example, the following command shows all the man pages that mention *open*.

```None
% man -k open
```

#### Learn More About Man Pages

The `man` command-line tool has its own man page, which is a good place to learn more about this feature:

```None
% man man
```

#### Revision History

- **2026-10-08** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3215-reading-man-pages)*