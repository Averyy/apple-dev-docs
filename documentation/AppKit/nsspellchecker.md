# NSSpellChecker

**Framework**: AppKit  
**Kind**: class

An interface to the Cocoa spell-checking service.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSSpellChecker
```

#### Overview

To handle all its spell checking, an app needs only one instance of [`NSSpellChecker`](nsspellchecker.md), known as the spell checker. Using the spell checker you manage the Spelling panel, in which the user can specify decisions about words that are suspect. The spell checker also offers the ability to provide word completions to augment the text completion system.

## Topics

### Getting the Spell Checker
- [class var shared: NSSpellChecker](nsspellchecker/shared.md)
  Returns the NSSpellChecker (one per application).
- [class var sharedSpellCheckerExists: Bool](nsspellchecker/sharedspellcheckerexists.md)
  Returns whether the application’s NSSpellChecker has already been created.
### Configuring Spell Checkers Languages
- [var availableLanguages: [String]](nsspellchecker/availablelanguages.md)
  Provides a list of all available languages.
- [var userPreferredLanguages: [String]](nsspellchecker/userpreferredlanguages.md)
  Provides a subset of the available languages to be used for spell checking.
- [var automaticallyIdentifiesLanguages: Bool](nsspellchecker/automaticallyidentifieslanguages.md)
  Sets whether the spell checker will automatically identify languages.
- [func language() -> String](nsspellchecker/language.md)
  Returns the current language used in spell checking.
- [func setLanguage(String) -> Bool](nsspellchecker/setlanguage(_:).md)
  Returns whether the specified language is in the Spelling pop-up list.
### Managing Panels
- [var spellingPanel: NSPanel](nsspellchecker/spellingpanel.md)
  Returns the spell checker’s panel.
- [var substitutionsPanel: NSPanel](nsspellchecker/substitutionspanel.md)
  Returns the substitutions panel.
- [func updateSpellingPanel(withGrammarString: String, detail: [String : Any])](nsspellchecker/updatespellingpanel(withgrammarstring:detail:).md)
  Specifies a grammar-analysis detail to highlight in the Spelling panel.
- [func updatePanels()](nsspellchecker/updatepanels.md)
  Updates the available panels to account for user changes.
- [var accessoryView: NSView?](nsspellchecker/accessoryview.md)
  Makes a view an accessory of the Spelling panel by making it a subview of the panel’s content view.
- [var substitutionsPanelAccessoryViewController: NSViewController?](nsspellchecker/substitutionspanelaccessoryviewcontroller.md)
  Sets the substitutions panel’s accessory view.
### Checking Strings for Spelling and Grammar
- [func countWords(in: String, language: String?) -> Int](nsspellchecker/countwords(in:language:).md)
  Returns the number of words in the specified string.
- [func checkSpelling(of: String, startingAt: Int) -> NSRange](nsspellchecker/checkspelling(of:startingat:).md)
  Starts the search for a misspelled word in `stringToCheck` starting at `startingOffset` within the string object.
- [func checkSpelling(of: String, startingAt: Int, language: String?, wrap: Bool, inSpellDocumentWithTag: Int, wordCount: UnsafeMutablePointer<Int>?) -> NSRange](nsspellchecker/checkspelling(of:startingat:language:wrap:inspelldocumentwithtag:wordcount:).md)
  Starts the search for a misspelled word in a string starting at specified offset within the string.
- [func checkGrammar(of: String, startingAt: Int, language: String?, wrap: Bool, inSpellDocumentWithTag: Int, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange](nsspellchecker/checkgrammar(of:startingat:language:wrap:inspelldocumentwithtag:details:).md)
  Initiates a grammatical analysis of a given string.
- [func check(String, range: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, orthography: AutoreleasingUnsafeMutablePointer<NSOrthography?>?, wordCount: UnsafeMutablePointer<Int>?) -> [NSTextCheckingResult]](nsspellchecker/check(_:range:types:options:inspelldocumentwithtag:orthography:wordcount:).md)
  Requests unified text checking for the given range of the given string.
- [func requestChecking(of: String, range: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult], NSOrthography, Int) -> Void)?) -> Int](nsspellchecker/requestchecking(of:range:types:options:inspelldocumentwithtag:completionhandler:).md)
  Requests that the string be checked in the background.
- [func guesses(forWordRange: NSRange, in: String, language: String?, inSpellDocumentWithTag: Int) -> [String]?](nsspellchecker/guesses(forwordrange:in:language:inspelldocumentwithtag:).md)
  Returns an array of possible substitutions for the specified string.
### Managing the Spell-Checking Process
- [class func uniqueSpellDocumentTag() -> Int](nsspellchecker/uniquespelldocumenttag.md)
  Returns a guaranteed unique tag to use as the spell-document tag for a document.
- [func closeSpellDocument(withTag: Int)](nsspellchecker/closespelldocument(withtag:).md)
  Notifies the receiver that the user has finished with the tagged document.
- [func ignoreWord(String, inSpellDocumentWithTag: Int)](nsspellchecker/ignoreword(_:inspelldocumentwithtag:).md)
  Instructs the spell checker to ignore all future occurrences of `wordToIgnore` in the document identified by `tag`.
- [func ignoredWords(inSpellDocumentWithTag: Int) -> [String]?](nsspellchecker/ignoredwords(inspelldocumentwithtag:).md)
  Returns the array of ignored words for a document identified by `tag`.
- [func setIgnoredWords([String], inSpellDocumentWithTag: Int)](nsspellchecker/setignoredwords(_:inspelldocumentwithtag:).md)
  Initializes the ignored-words document (a dictionary identified by `tag` with `someWords`), an array of words to ignore.
- [func setWordFieldStringValue(String)](nsspellchecker/setwordfieldstringvalue(_:).md)
  Sets the string that appears in the misspelled word field, using the string object `aString`.
- [func updateSpellingPanel(withMisspelledWord: String)](nsspellchecker/updatespellingpanel(withmisspelledword:).md)
  Causes the spell checker to update the Spelling panel’s misspelled-word field to reflect `word`.
- [func completions(forPartialWordRange: NSRange, in: String, language: String?, inSpellDocumentWithTag: Int) -> [String]?](nsspellchecker/completions(forpartialwordrange:in:language:inspelldocumentwithtag:).md)
  Provides a list of complete words that the user might be trying to type based on a partial word in a given string.
- [func hasLearnedWord(String) -> Bool](nsspellchecker/haslearnedword(_:).md)
  Indicates whether the spell checker has learned a given word.
- [func unlearnWord(String)](nsspellchecker/unlearnword(_:).md)
  Tells the spell checker to unlearn a given word.
- [func learnWord(String)](nsspellchecker/learnword(_:).md)
  Adds the word to the spell checker dictionary.
- [func userQuotesArray(forLanguage: String) -> [String]](nsspellchecker/userquotesarray(forlanguage:).md)
  Returns the default values for quote replacement.
- [var userReplacementsDictionary: [String : String]](nsspellchecker/userreplacementsdictionary.md)
  Returns the dictionary used when replacing words.
### Data Detector Interaction
- [func menu(for: NSTextCheckingResult, string: String, options: [NSSpellChecker.OptionKey : Any]?, atLocation: NSPoint, in: NSView) -> NSMenu?](nsspellchecker/menu(for:string:options:atlocation:in:).md)
  Provides a menu containing contextual menu items suitable for certain kinds of detected results.
- [NSSpellChecker.OptionKey](nsspellchecker/optionkey.md)
  The constants are optional keys that can be used in the options dictionary parameter of the [`check(_:range:types:options:inSpellDocumentWithTag:orthography:wordCount:)`](nsspellchecker/check(_:range:types:options:inspelldocumentwithtag:orthography:wordcount:).md), [`requestChecking(of:range:types:options:inSpellDocumentWithTag:completionHandler:)`](nsspellchecker/requestchecking(of:range:types:options:inspelldocumentwithtag:completionhandler:).md), and [`menu(for:string:options:atLocation:in:)`](nsspellchecker/menu(for:string:options:atlocation:in:).md) methods.
### Automatic Spelling Correction
- [func correction(forWordRange: NSRange, in: String, language: String, inSpellDocumentWithTag: Int) -> String?](nsspellchecker/correction(forwordrange:in:language:inspelldocumentwithtag:).md)
  Returns a single proposed correction if a word is mis-spelled.
- [func showCorrectionIndicator(of: NSSpellChecker.CorrectionIndicatorType, primaryString: String, alternativeStrings: [String], forStringIn: NSRect, view: NSView, completionHandler: ((String?) -> Void)?)](nsspellchecker/showcorrectionindicator(of:primarystring:alternativestrings:forstringin:view:completionhandler:).md)
  Display a suitable user interface to indicate a correction may need to be made.
- [func record(NSSpellChecker.CorrectionResponse, toCorrection: String, forWord: String, language: String?, inSpellDocumentWithTag: Int)](nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:).md)
  Records the user response to the correction indicator being displayed.
- [func dismissCorrectionIndicator(for: NSView)](nsspellchecker/dismisscorrectionindicator(for:).md)
  Dismisses the correction indicator for the specified view.
- [NSSpellChecker.CorrectionIndicatorType](nsspellchecker/correctionindicatortype.md)
  Constants that allow an app to specify the correction indicator type displayed.
- [NSSpellChecker.CorrectionResponse](nsspellchecker/correctionresponse.md)
  The correction response passed to the[`record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)`](nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:).md) method.
### Notifications
- [class let didChangeAutomaticSpellingCorrectionNotification: NSNotification.Name](nsspellchecker/didchangeautomaticspellingcorrectionnotification.md)
  This notification is posted when the spell checker did change text using automatic spell checking correction. The are posted to the application’s default notification center.
- [class let didChangeAutomaticTextReplacementNotification: NSNotification.Name](nsspellchecker/didchangeautomatictextreplacementnotification.md)
  Posted when the spell checker changed text using automatic text replacement.  This notification is posted to the app’s default notification center.
### Type Properties
- [class let didChangeAutomaticCapitalizationNotification: NSNotification.Name](nsspellchecker/didchangeautomaticcapitalizationnotification.md)
- [class let didChangeAutomaticDashSubstitutionNotification: NSNotification.Name](nsspellchecker/didchangeautomaticdashsubstitutionnotification.md)
- [class let didChangeAutomaticPeriodSubstitutionNotification: NSNotification.Name](nsspellchecker/didchangeautomaticperiodsubstitutionnotification.md)
- [class let didChangeAutomaticQuoteSubstitutionNotification: NSNotification.Name](nsspellchecker/didchangeautomaticquotesubstitutionnotification.md)
- [class let didChangeAutomaticTextCompletionNotification: NSNotification.Name](nsspellchecker/didchangeautomatictextcompletionnotification.md)
- [class var isAutomaticCapitalizationEnabled: Bool](nsspellchecker/isautomaticcapitalizationenabled.md)
- [class var isAutomaticDashSubstitutionEnabled: Bool](nsspellchecker/isautomaticdashsubstitutionenabled.md)
- [class var isAutomaticInlinePredictionEnabled: Bool](nsspellchecker/isautomaticinlinepredictionenabled.md)
- [class var isAutomaticPeriodSubstitutionEnabled: Bool](nsspellchecker/isautomaticperiodsubstitutionenabled.md)
- [class var isAutomaticQuoteSubstitutionEnabled: Bool](nsspellchecker/isautomaticquotesubstitutionenabled.md)
- [class var isAutomaticSpellingCorrectionEnabled: Bool](nsspellchecker/isautomaticspellingcorrectionenabled.md)
- [class var isAutomaticTextCompletionEnabled: Bool](nsspellchecker/isautomatictextcompletionenabled.md)
- [class var isAutomaticTextReplacementEnabled: Bool](nsspellchecker/isautomatictextreplacementenabled.md)
### Instance Methods
- [func deletesAutospaceBetweenString(String, andString: String, language: String?) -> Bool](nsspellchecker/deletesautospacebetweenstring(_:andstring:language:).md)
- [func language(forWordRange: NSRange, in: String, orthography: NSOrthography?) -> String?](nsspellchecker/language(forwordrange:in:orthography:).md)
- [func preventsAutocorrection(before: String, language: String?) -> Bool](nsspellchecker/preventsautocorrection(before:language:).md)
- [func requestCandidates(forSelectedRange: NSRange, in: String, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult]) -> Void)?) -> Int](nsspellchecker/requestcandidates(forselectedrange:in:types:options:inspelldocumentwithtag:completionhandler:).md)
- [func showInlinePrediction(forCandidates: [NSTextCheckingResult], client: any NSTextInputClient)](nsspellchecker/showinlineprediction(forcandidates:client:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSChangeSpelling](nschangespelling.md)
  A protocol that responder objects can implement to correct a misspelled word.
- [protocol NSIgnoreMisspelledWords](nsignoremisspelledwords.md)
  A protocol that enables the Ignore button in the Spelling panel to function properly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker)*